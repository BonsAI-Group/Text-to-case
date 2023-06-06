class ITextToNum:
    """Interface for Text to Numeric library."""
    def __init__(self) -> None:
        pass
    
    def textToNum(self, predicted_answer: str) -> int:
        """Converts text to represent its digit. Returns numerical word digit."""
        raise NotImplementedError
    
