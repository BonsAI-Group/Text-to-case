from typing import Tuple

from models import MultiAnswer


class IMultiChoiceModel:
    """Interface for multi-choice models."""
    def __init__(self) -> None:
        pass
    
    def answerMultiChoice(self, candidate_labels: list, context: str) -> MultiAnswer:
        """Answer a multi-choice question given a context and labels. Returns the confidence for each label."""
        raise NotImplementedError
    
