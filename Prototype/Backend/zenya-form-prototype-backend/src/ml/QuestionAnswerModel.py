from typing import Tuple
import requests
from transformers import pipeline

def query(model, payload):
    response = requests.post(
        model, 
        headers={
            'Authorization':'Bearer K64489zyHzCgPHmi3nFufOequK519ajO',
        }, 
        json=payload
    )
    return response.json()

class QuestionAnswerModel:
    _instances = {}

    """Contains a single question answering model"""
    def __init__(self, model_path):
        # from transformers import pipeline
        # self.model = pipeline("question-answering", model=model_path, tokenizer=model_path)
        self.model = model_path
    
    def answerQuestion(self, question: str, context: str) -> Tuple[str, float]:
        """Answer a question given a context. Returns the answer and the confidence."""
        result = query(self.model, {
            "inputs": {
                "question": question,
                "context": context
            }
        })
        return result["answer"], result["score"]
