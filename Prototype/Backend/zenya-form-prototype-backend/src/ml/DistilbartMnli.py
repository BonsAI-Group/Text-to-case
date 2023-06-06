from .IRadioButtonModel import IRadioButtonModel
from .RadioButtonModel import RadioButtonModel
from models.Answer import Answer

class DistilbartRadioChoice(IRadioButtonModel):
    """A Question Answering model that uses a single BERT Large model."""
    def __init__(self):
        self.model = RadioButtonModel("valhalla/distilbart-mnli-12-1")
        self.treshhold = .26

    def answerRadioButton(self, candidate_labels: list, context: str) -> Answer:
        """Answer a question given a context. Returns the answer and the confidence.""" 
        sequence, labels, scores = self.model.answerRadioButton(context, candidate_labels)
        highest_score = max(scores)
        highest_score_index = scores.index(highest_score)
        highest_score_trusted = True if highest_score > self.treshhold else False
        return Answer(answer=labels[highest_score_index], confidence=highest_score, isTrusted=highest_score_trusted)
        
