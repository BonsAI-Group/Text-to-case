from typing import Tuple

from models.MultiAnswer import MultiAnswer


class MultiChoiceModel:
    _instances = {}

    """Contains a single multi-choice model"""
    def __init__(self, model_path):
        self.model_path = model_path
        from transformers import pipeline
        self.model = pipeline("zero-shot-classification", model=model_path)
    
    def answerMultiChoice(self, candidate_labels: list, context: str) -> MultiAnswer:
        """Answer a multi-choice question given a context and labels. Returns the confidence for each label."""
        result = self.model(context, candidate_labels, multi_label = True)
        ordered_labels = []
        ordered_scores = []
        for label in candidate_labels:
            ordered_labels.append(label)
            ordered_scores.append(result["scores"][result["labels"].index(label)])
        return MultiAnswer(answers=ordered_labels, confidence=ordered_scores, isTrusted=[])
    
    # To make this class a singleton if a class with that model_path already exists
    def __new__(cls, model_path):
        if model_path not in cls._instances:
            cls._instances[model_path] = super(MultiChoiceModel, cls).__new__(cls)
        return cls._instances[model_path]