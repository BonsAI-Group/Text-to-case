class QuestionAnswerModel:
    """Contains a single question answering model"""
    def __init__(self, model_path):
        from transformers import pipeline
        self.model = pipeline("question-answering", model=model_path, tokenizer=model_path)
    
    def answerQuestion(self, question: str, context: str) -> tuple[str, float]:
        """Answer a question given a context. Returns the answer and the confidence."""
        result = self.model(question=question, context=context)
        return result["answer"], result["score"]