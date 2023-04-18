from typing import Tuple
from .IMultiChoiceModel import IMultiChoiceModel
from .MultiChoiceModel import MultiChoiceModel
from .IRadioButtonModel import IRadioButtonModel
from .RadioButtonModel import RadioButtonModel


class DestilbertBaseSingleModelMultiChoice(IMultiChoiceModel, IRadioButtonModel):
    """A Question Answering model that uses a single BERT Large model."""
    def __init__(self):
        self.multiChoiceModel = MultiChoiceModel("typeform/distilbert-base-uncased-mnli")
        self.radioModel = RadioButtonModel("typeform/distilbert-base-uncased-mnli")

    def answerMultiChoice(self, candidate_labels: list, context: str) -> Tuple[str, float]:
        """Answer a question given a context. Returns the answer and the confidence.""" 
        return self.multiChoiceModel.answerMultiChoice(context, candidate_labels)

    def answerRadioButton(self, candidate_labels: list, context: str) -> Tuple[str, float]:
        """Answer a question given a context. Returns the answer and the confidence.""" 
        return self.radioModel.answerRadioButton(context, candidate_labels)
    