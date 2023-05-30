from typing import Tuple

from models.MultiAnswer import MultiAnswer
from .IMultiChoiceModel import IMultiChoiceModel
from .MultiChoiceModel import MultiChoiceModel


class DabertaLargeMultiChoice(IMultiChoiceModel):
    """A Question Answering model that uses a single BERT Large model."""
    def __init__(self):
        self.model = MultiChoiceModel("microsoft/deberta-large-mnli")
        self.treshhold = .6

    def answerMultiChoice(self, candidate_labels: list, context: str) -> MultiAnswer:
        """Answer a question given a context. Returns the answer and the confidence.""" 
        answer: MultiAnswer = self.model.answerMultiChoice(context, candidate_labels)
        # return MultiAnswer(answers=answer.answers, confidence=answer.confidence, isTrusted=[True for _ in range(len(answer.answers))])
        return MultiAnswer(
            answers=answer.answers, 
            confidence=answer.confidence, 
            isTrusted=[confidence >= self.treshhold for confidence in answer.confidence]
        )
    