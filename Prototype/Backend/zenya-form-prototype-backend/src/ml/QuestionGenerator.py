from .IQuestionGenerator import IQuestionGenerator
from transformers import T5ForConditionalGeneration, T5Tokenizer

class QuestionGenerator(IQuestionGenerator):
    def __init__(self, formName: str):
        self.formName = formName

    def generateQuestion(self, fieldName: str):
        model_name = "allenai/t5-small-squad2-question-generation"
        tokenizer = T5Tokenizer.from_pretrained(model_name)
        model = T5ForConditionalGeneration.from_pretrained(model_name)

        input_ids = tokenizer.encode(f"create a question to ask what, who, where, when, why, how many, how much, how, whose or which the {fieldName} is for the {self.formName}", return_tensors="pt")
        res = model.generate(input_ids)
        output = tokenizer.batch_decode(res, skip_special_tokens=True)
        print(output)
        return output if not None else ""

