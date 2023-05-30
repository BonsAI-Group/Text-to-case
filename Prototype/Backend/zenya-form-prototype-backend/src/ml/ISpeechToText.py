import wave

class ISpeechToText:
    """Interface for Speech to Text library."""
    def __init__(self) -> None:
        pass
    
    def speechToText(self, spoken_context: wave) -> str:
        """Converts spoken text to represent context format written. Returns written context of the spoken text."""
        raise NotImplementedError
    
