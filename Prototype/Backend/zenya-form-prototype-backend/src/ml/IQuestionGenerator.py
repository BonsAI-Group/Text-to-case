class IQuestionGenerator:
    """Interface for question generators."""
    def __init__(self) -> None:
        pass
    
    def generateQuestion(self, fieldName: str) -> str:
        """Generate a question given a field name."""
        raise NotImplementedError