from typing import Tuple

from models import Answer


class IRadioButtonModel:
    """Interface for radio button models."""
    def __init__(self) -> None:
        pass
    
    def answerRadioButton(self, candidate_labels: list, context: str) -> Answer:
        """Answer a radio button question given a context and labels. Returns the confidence for each label."""
        raise NotImplementedError
    
