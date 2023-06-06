from .ITextToNum import ITextToNum
from text_to_num import alpha2digit
import re

class TextToNum(ITextToNum):
    def __init__(self ):
        self

    def textToNum(self, predicted_answer: str) -> str:
        numeric_answer = alpha2digit(predicted_answer, "en")
        # Finding first number
        numeric_answer = re.search(r'\d+', numeric_answer)  
        if numeric_answer:
            # Printing number and its index 
            print('The first number is:', numeric_answer.group())
            numeric_answer = numeric_answer.group()
        else:
            print('The given string does not have any number') 
            numeric_answer= 0 
        return numeric_answer