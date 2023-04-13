from typing import Tuple

from models.Answer import Answer


class IQuestionAnswerer:
    """Interface for Question Answering models."""
    def __init__(self) -> None:
        pass
    
    def answerQuestion(self, question: str, context: str) -> Answer:
        """Answer a question given a context. Returns the answer and the confidence."""
        raise NotImplementedError
    
