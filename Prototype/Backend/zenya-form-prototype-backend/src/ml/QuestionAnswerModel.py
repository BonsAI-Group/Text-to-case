from typing import Tuple
import requests
from service.ModelRequesterService import ModelRequesterService

class QuestionAnswerModel:
    _instances = {}

    """Contains a single question answering model"""
    def __init__(self, model_path):
        self.model = model_path
    
    def answerQuestion(self, question: str, context: str) -> Tuple[str, float]:
        """Answer a question given a context. Returns the answer and the confidence."""
        answer, score = ModelRequesterService.RequestQuestionAnswering(model=self.model, question=question, context=context)
        # print(result)
        return answer, score
