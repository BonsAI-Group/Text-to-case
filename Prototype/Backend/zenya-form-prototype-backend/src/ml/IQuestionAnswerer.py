class IQuestionAnswerer:
    """Interface for Question Answering models."""
    def __init__(self) -> None:
        pass
    
    def answerQuestion(self, question: str, context: str) -> tuple[str, float]:
        """Answer a question given a context. Returns the answer and the confidence."""
        raise NotImplementedError
    
