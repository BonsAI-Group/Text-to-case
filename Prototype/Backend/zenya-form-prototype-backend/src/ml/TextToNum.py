from .ITextToNum import ITextToNum
from text_to_num import alpha2digit
import re

class TextToNum(ITextToNum):
    def __init__(self ):
        self

    def textToNum(self, predicted_answer: str) -> str:
        numeric_answer = alpha2digit(predicted_answer, "en")
        numeric_answer = re.sub("\D","",numeric_answer)
        return numeric_answer