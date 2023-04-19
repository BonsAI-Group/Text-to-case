class MultiChoiceAnswer():
    def __init__(self, labels: list[str], confidences: list[float]):
        self.labels = labels
        self.confidences = confidences