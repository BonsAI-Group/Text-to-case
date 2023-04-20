from typing import Tuple

from models.MultiAnswer import MultiAnswer
from models.Answer import Answer
from .IMultiChoiceModel import IMultiChoiceModel
from .MultiChoiceModel import MultiChoiceModel
from .IRadioButtonModel import IRadioButtonModel
from .RadioButtonModel import RadioButtonModel


class DestilbertBaseSingleModelMultiChoice(IMultiChoiceModel, IRadioButtonModel):
    """A Question Answering model that uses a single BERT Large model."""
    def __init__(self):
        self.multiChoiceModel = MultiChoiceModel("typeform/distilbert-base-uncased-mnli")
        self.radioModel = RadioButtonModel("typeform/distilbert-base-uncased-mnli")

    def answerMultiChoice(self, candidate_labels: list, context: str) -> MultiAnswer:
        """Answer a question given a context. Returns the answer and the confidence.""" 
        sequence, labels, scores = self.multiChoiceModel.answerMultiChoice(context, candidate_labels)
        return MultiAnswer(answers=labels, confidence=scores, isTrusted=[True for _ in range(len(sequence))])

    def answerRadioButton(self, candidate_labels: list, context: str) -> Answer:
        """Answer a question given a context. Returns the answer and the confidence.""" 
        sequence, labels, scores = self.radioModel.answerRadioButton(context, candidate_labels)
        highest_score = max(scores)
        highest_score_index = scores.index(highest_score)
        return Answer(answer=labels[highest_score_index], confidence=highest_score, isTrusted=True)
    