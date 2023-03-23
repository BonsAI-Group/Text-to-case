from transformers import pipeline
from ..models.form import Form
from ..models.form_item import FormItem
from ..models.form_answer import FormAnswer

"""
Basic QA class

This is just an initial example of a class that does the QA process. Later this will be replaced by a proper pipeline that includes question generating and answering.
"""
class BasicQA: 
    def __init__(self):
        self.model = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad", tokenizer="bert-large-uncased-whole-word-masking-finetuned-squad")

    def answer_question(self, question, context):
        return self.model(question=question, context=context)
    
    def answer_form(self, context: str, form: Form) -> FormAnswer:
        answers: dict[str, str] = {}
        for item in form.fields:
            answers[item.fieldName] = self.answer_question(item.fieldName, context)["answer"]
        
        return FormAnswer(answers=answers)