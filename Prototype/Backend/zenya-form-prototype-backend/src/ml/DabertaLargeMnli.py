from typing import Tuple

from models.MultiAnswer import MultiAnswer
from models.Answer import Answer
from .IMultiChoiceModel import IMultiChoiceModel
from .MultiChoiceModel import MultiChoiceModel
from .IRadioButtonModel import IRadioButtonModel
from .RadioButtonModel import RadioButtonModel


class DabertaLargeMultiChoice(IMultiChoiceModel, IRadioButtonModel):
    """A Question Answering model that uses a single BERT Large model."""
    def __init__(self):
        self.multiChoiceModel = MultiChoiceModel("microsoft/deberta-large-mnli")
        self.radioModel = RadioButtonModel("valhalla/distilbart-mnli-12-1")

    def answerMultiChoice(self, candidate_labels: list, context: str) -> MultiAnswer:
        """Answer a question given a context. Returns the answer and the confidence.""" 
        answer: MultiAnswer = self.multiChoiceModel.answerMultiChoice(context, candidate_labels)
        # return MultiAnswer(answers=answer.answers, confidence=answer.confidence, isTrusted=[True for _ in range(len(answer.answers))])
        return MultiAnswer(
            answers=answer.answers, 
            confidence=answer.confidence, 
            isTrusted=[confidence >= .6 for confidence in answer.confidence]
        )

    def answerRadioButton(self, candidate_labels: list, context: str) -> Answer:
        """Answer a question given a context. Returns the answer and the confidence.""" 
        sequence, labels, scores = self.radioModel.answerRadioButton(context, candidate_labels)
        highest_score = max(scores)
        highest_score_index = scores.index(highest_score)
        highest_score_trusted = True if highest_score > .26 else False
        return Answer(answer=labels[highest_score_index], confidence=highest_score, isTrusted=highest_score_trusted)
    