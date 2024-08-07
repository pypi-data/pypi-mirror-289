import logging
from typing import Callable, ClassVar, Dict, List, Optional, Tuple, Union

import numpy as np
import pydantic
from trulens.core.utils.imports import OptionalImports
from trulens.core.utils.imports import format_import_errors
from trulens.core.utils.pyschema import FunctionOrMethod
from trulens.core.utils.pyschema import WithClassInfo
from trulens.core.utils.serial import SerialModel
from trulens.feedback.generated import re_0_10_rating
from trulens.feedback.llm_provider import LLMProvider

with OptionalImports(
    messages=format_import_errors("bert-score", purpose="measuring BERT Score")
):
    from bert_score import BERTScorer

with OptionalImports(
    messages=format_import_errors("evaluate", purpose="using certain metrics")
):
    import evaluate

logger = logging.getLogger(__name__)


# TODEP
class GroundTruthAgreement(WithClassInfo, SerialModel):
    """
    Measures Agreement against a Ground Truth.
    """

    ground_truth: Union[List[Dict], FunctionOrMethod]
    provider: LLMProvider

    # Note: the bert scorer object isn't serializable
    # It's a class member because creating it is expensive
    bert_scorer: object

    ground_truth_imp: Optional[Callable] = pydantic.Field(None, exclude=True)

    model_config: ClassVar[dict] = dict(arbitrary_types_allowed=True)

    def __init__(
        self,
        ground_truth: Union[List, Callable, FunctionOrMethod],
        provider: LLMProvider,
        bert_scorer: Optional["BERTScorer"] = None,
        **kwargs,
    ):
        """Measures Agreement against a Ground Truth.

        Usage 1:
        ```
        from trulens.feedback import GroundTruthAgreement
        from trulens.providers.openai import OpenAI
        golden_set = [
            {"query": "who invented the lightbulb?", "response": "Thomas Edison"},
            {"query": "¿quien invento la bombilla?", "response": "Thomas Edison"}
        ]
        ground_truth_collection = GroundTruthAgreement(golden_set, provider=OpenAI())
        ```

        Usage 2:
        ```
        from trulens.feedback import GroundTruthAgreement
        from trulens.providers.cortex import Cortex
        ground_truth_imp = llm_app
        response = llm_app(prompt)

        ground_truth_collection = GroundTruthAgreement(ground_truth_imp, provider=Cortex(model_engine="mistral-7b"))
        ```

        Args:
            ground_truth (Union[Callable, FunctionOrMethod]): A list of query/response pairs or a function or callable that returns a ground truth string given a prompt string.
            provider (LLMProvider): The provider to use for agreement measures.
            bert_scorer (Optional[&quot;BERTScorer&quot;], optional): Internal Usage for DB serialization.

        """
        if isinstance(ground_truth, List):
            ground_truth_imp = None
        elif isinstance(ground_truth, FunctionOrMethod):
            ground_truth_imp = ground_truth.load()
        elif isinstance(ground_truth, Callable):
            ground_truth_imp = ground_truth
            ground_truth = FunctionOrMethod.of_callable(ground_truth)
        elif isinstance(ground_truth, Dict):
            # Serialized FunctionOrMethod?
            ground_truth = FunctionOrMethod.model_validate(ground_truth)
            ground_truth_imp = ground_truth.load()
        else:
            raise RuntimeError(
                f"Unhandled ground_truth type: {type(ground_truth)}."
            )

        super().__init__(
            ground_truth=ground_truth,
            ground_truth_imp=ground_truth_imp,
            provider=provider,
            bert_scorer=bert_scorer,
            **kwargs,
        )

    def _find_response(self, prompt: str) -> Optional[str]:
        if self.ground_truth_imp is not None:
            return self.ground_truth_imp(prompt)

        responses = [
            qr["response"] for qr in self.ground_truth if qr["query"] == prompt
        ]
        if responses:
            return responses[0]
        else:
            return None

    def _find_score(self, prompt: str, response: str) -> Optional[float]:
        if self.ground_truth_imp is not None:
            return self.ground_truth_imp(prompt)

        responses = [
            qr["expected_score"]
            for qr in self.ground_truth
            if qr["query"] == prompt and qr["response"] == response
        ]
        if responses:
            return responses[0]
        else:
            return None

    # TODEP
    def agreement_measure(
        self, prompt: str, response: str
    ) -> Union[float, Tuple[float, Dict[str, str]]]:
        """
        Uses OpenAI's Chat GPT Model. A function that that measures
        similarity to ground truth. A second template is given to Chat GPT
        with a prompt that the original response is correct, and measures
        whether previous Chat GPT's response is similar.

        Example:

            ```python
            from trulens.core import Feedback
            from trulens.feedback import GroundTruthAgreement
            from trulens.providers.openai import OpenAI

            golden_set = [
                {"query": "who invented the lightbulb?", "response": "Thomas Edison"},
                {"query": "¿quien invento la bombilla?", "response": "Thomas Edison"}
            ]
            ground_truth_collection = GroundTruthAgreement(golden_set, provider=OpenAI())

            feedback = Feedback(ground_truth_collection.agreement_measure).on_input_output()
            ```
            The `on_input_output()` selector can be changed. See [Feedback Function Guide](https://www.trulens.org/trulens/feedback_function_guide/)

        Args:
            prompt (str): A text prompt to an agent.
            response (str): The agent's response to the prompt.

        Returns:
            - float: A value between 0 and 1. 0 being "not in agreement" and 1
                being "in agreement".
            - dict: with key 'ground_truth_response'
        """
        ground_truth_response = self._find_response(prompt)
        if ground_truth_response:
            agreement_txt = self.provider._get_answer_agreement(
                prompt, response, ground_truth_response
            )
            ret = (
                re_0_10_rating(agreement_txt) / 10,
                dict(ground_truth_response=ground_truth_response),
            )
        else:
            ret = np.nan

        return ret

    def absolute_error(self, prompt: str, response: str, score: float) -> float:
        """
        Method to look up the numeric expected score from a golden set and take the difference.

        Primarily used for evaluation of model generated feedback against human feedback

        Example:

            ```python
            from trulens.core import Feedback
            from trulens.feedback import GroundTruthAgreement
            from trulens.providers.bedrock import Bedrock

            golden_set =
            {"query": "How many stomachs does a cow have?", "response": "Cows' diet relies primarily on grazing.", "expected_score": 0.4},
            {"query": "Name some top dental floss brands", "response": "I don't know", "expected_score": 0.8}
            ]

            bedrock = Bedrock(
                model_id="amazon.titan-text-express-v1", region_name="us-east-1"
            )
            ground_truth_collection = GroundTruthAgreement(golden_set, provider=bedrock)

            f_groundtruth = Feedback(ground_truth.absolute_error.on(Select.Record.calls[0].args.args[0]).on(Select.Record.calls[0].args.args[1]).on_output()
            ```

        """

        expected_score = self._find_score(prompt, response)
        if expected_score is not None:
            ret = abs(float(score) - float(expected_score))
            expected_score = (
                "{:.2f}".format(expected_score).rstrip("0").rstrip(".")
            )
        else:
            ret = np.nan
        return ret, {"expected score": expected_score}

    def bert_score(
        self, prompt: str, response: str
    ) -> Union[float, Tuple[float, Dict[str, str]]]:
        """
        Uses BERT Score. A function that that measures
        similarity to ground truth using bert embeddings.

        Example:

            ```python
            from trulens.core import Feedback
            from trulens.feedback import GroundTruthAgreement
            from trulens.providers.openai import OpenAI
            golden_set = [
                {"query": "who invented the lightbulb?", "response": "Thomas Edison"},
                {"query": "¿quien invento la bombilla?", "response": "Thomas Edison"}
            ]
            ground_truth_collection = GroundTruthAgreement(golden_set, provider=OpenAI())

            feedback = Feedback(ground_truth_collection.bert_score).on_input_output()
            ```
            The `on_input_output()` selector can be changed. See [Feedback Function Guide](https://www.trulens.org/trulens/feedback_function_guide/)


        Args:
            prompt (str): A text prompt to an agent.
            response (str): The agent's response to the prompt.

        Returns:
            - float: A value between 0 and 1. 0 being "not in agreement" and 1
                being "in agreement".
            - dict: with key 'ground_truth_response'
        """
        if self.bert_scorer is None:
            self.bert_scorer = BERTScorer(lang="en", rescale_with_baseline=True)
        ground_truth_response = self._find_response(prompt)
        if ground_truth_response:
            bert_score = self.bert_scorer.score(
                [response], [ground_truth_response]
            )
            ret = (
                bert_score[0].item(),
                dict(ground_truth_response=ground_truth_response),
            )
        else:
            ret = np.nan

        return ret

    # TODEP
    def bleu(
        self, prompt: str, response: str
    ) -> Union[float, Tuple[float, Dict[str, str]]]:
        """
        Uses BLEU Score. A function that that measures
        similarity to ground truth using token overlap.

        Example:

            ```python
            from trulens.core import Feedback
            from trulens.feedback import GroundTruthAgreement
            from trulens.providers.openai import OpenAI
            golden_set = [
                {"query": "who invented the lightbulb?", "response": "Thomas Edison"},
                {"query": "¿quien invento la bombilla?", "response": "Thomas Edison"}
            ]
            ground_truth_collection = GroundTruthAgreement(golden_set, provider=OpenAI())

            feedback = Feedback(ground_truth_collection.bleu).on_input_output()
            ```
            The `on_input_output()` selector can be changed. See [Feedback Function Guide](https://www.trulens.org/trulens/feedback_function_guide/)

        Args:
            prompt (str): A text prompt to an agent.
            response (str): The agent's response to the prompt.

        Returns:
            - float: A value between 0 and 1. 0 being "not in agreement" and 1
                being "in agreement".
            - dict: with key 'ground_truth_response'
        """
        bleu = evaluate.load("bleu")
        ground_truth_response = self._find_response(prompt)
        if ground_truth_response:
            bleu_score = bleu.compute(
                predictions=[response], references=[ground_truth_response]
            )
            ret = (
                bleu_score["bleu"],
                dict(ground_truth_response=ground_truth_response),
            )
        else:
            ret = np.nan

        return ret

    # TODEP
    def rouge(
        self, prompt: str, response: str
    ) -> Union[float, Tuple[float, Dict[str, str]]]:
        """
        Uses BLEU Score. A function that that measures
        similarity to ground truth using token overlap.

        Args:
            prompt (str): A text prompt to an agent.
            response (str): The agent's response to the prompt.

        Returns:
            - float: A value between 0 and 1. 0 being "not in agreement" and 1
                being "in agreement".
            - dict: with key 'ground_truth_response'
        """
        rouge = evaluate.load("rouge")
        ground_truth_response = self._find_response(prompt)
        if ground_truth_response:
            rouge_score = rouge.compute(
                predictions=[response], references=[ground_truth_response]
            )
            ret = (
                rouge_score["rouge1"],
                dict(ground_truth_response=ground_truth_response),
            )
        else:
            ret = np.nan

        return ret
