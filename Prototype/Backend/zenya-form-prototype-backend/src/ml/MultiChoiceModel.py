from typing import Tuple

from models.MultiAnswer import MultiAnswer


class MultiChoiceModel:
    """Contains a single multi-choice model"""
    def __init__(self, model_path):
        from transformers import pipeline
        self.model = pipeline(model=model_path)
    
    def answerMultiChoice(self, candidate_labels: list, context: str) -> MultiAnswer:
        """Answer a multi-choice question given a context and labels. Returns the confidence for each label."""
        result = self.model(context, candidate_labels=candidate_labels, multi_label = True)
        ordered_labels = []
        ordered_scores = []
        for label in candidate_labels:
            ordered_labels.append(label)
            ordered_scores.append(result["scores"][result["labels"].index(label)])
        return MultiAnswer(answers=ordered_labels, confidence=ordered_scores, isTrusted=[])