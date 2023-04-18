from typing import Tuple


class MultiChoiceModel:
    """Contains a single multi-choice model"""
    def __init__(self, model_path):
        from transformers import pipeline
        self.model = pipeline(model=model_path)
    
    def answerMultiChoice(self, candidate_labels: list, context: str) -> Tuple[str, float]:
        """Answer a multi-choice question given a context and labels. Returns the confidence for each label."""
        result = self.model(context, candidate_labels=candidate_labels, multi_label = True)
        return result["sequence"], result["labels"], result["scores"]