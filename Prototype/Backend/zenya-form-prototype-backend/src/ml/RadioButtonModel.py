from typing import Tuple

class RadioButtonModel:
    """Contains a single radio button model"""
    def __init__(self, model_path):
        from transformers import pipeline
        self.model = pipeline(model=model_path)
    
    def answerRadioButton(self, candidate_labels: list, context: str) -> Tuple[str, float]:
        """Answer a radio button question given a context and labels. Returns the confidence for each label."""
        result = self.model(context, candidate_labels=candidate_labels)
        return result["sequence"], result["labels"], result["scores"]