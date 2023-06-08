from typing import Tuple
from service.ModelRequesterService import ModelRequesterService

class RadioButtonModel:
    _instances = {}
    """Contains a single radio button model"""
    def __init__(self, model_path):
        self.model_path = model_path
    
    def answerRadioButton(self, candidate_labels: list, context: str) -> Tuple[str, float]:
        """Answer a radio button question given a context and labels. Returns the confidence for each label."""
        result = ModelRequesterService.RequestMultipleChoice(model=self.model_path, candidate_labels=candidate_labels, context=context)
        return result["labels"], result["scores"]
    
    # To make this class a singleton if a class with that model_path already exists
    def __new__(cls, model_path):
        if model_path not in cls._instances:
            cls._instances[model_path] = super(RadioButtonModel, cls).__new__(cls)
        return cls._instances[model_path]