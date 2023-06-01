import wave
from ml.SpeechToText import SpeechToText
from ml.ISpeechToText import ISpeechToText
import os

class SpeechToTextService:
    """Service for handling fields."""
    def __init__(self):
        self.SpeechToText: ISpeechToText = SpeechToText()

    def fillInSpeechToText(self, audio_file: wave) -> str:
        path = os.getcwd() + '//audio_files//recording.wav'
        self.SpeechToText.speechToText(path)
        