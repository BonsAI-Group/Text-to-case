from typing import Tuple
from transformers import pipeline

class QuestionAnswerModel:
    _instances = {}

    """Contains a single question answering model"""
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = pipeline("question-answering", model=model_path, tokenizer=model_path)
    
    def answerQuestion(self, question: str, context: str) -> Tuple[str, float]:
        """Answer a question given a context. Returns the answer and the confidence."""
        result = self.model(question=question, context=context)
        return result["answer"], result["score"]
    
    # To make this class a singleton if a class with that model_path already exists
    def __new__(cls, model_path):
        if model_path not in cls._instances:
            cls._instances[model_path] = super(QuestionAnswerModel, cls).__new__(cls)
        return cls._instances[model_path]