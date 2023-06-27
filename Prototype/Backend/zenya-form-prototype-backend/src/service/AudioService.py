from fastapi import UploadFile
from ml.IQuestionGenerator import IQuestionGenerator
from ml.InterrogativeQuestionGenerator import InterrogativeQuestionGenerator
from ml.InterrogativeQuestionGenerator import InterrogativeQuestionGenerator
from ml.SpeechToText import SpeechToText
from ml.ISpeechToText import ISpeechToText

class AudioService:
    """Service for handling fields."""
    def __init__(self):
        self.QuestionGenerator: IQuestionGenerator = InterrogativeQuestionGenerator()
        self.SpeechToText: ISpeechToText = SpeechToText()

    def fillInAudioToText(self, spoken_context: bytes) -> str:
        """Fill in spoken context."""
        """Checking the field Type"""
        return(self.SpeechToText.speechToText(spoken_context))
        
        