from fastapi import FastAPI
from transformers import pipeline
from RequestModels.question_answering_request import QuestionAnsweringRequest
from RequestModels.multiple_choice_request import MultipleChoiceRequest
app = FastAPI()

models = {
    "deepset/deberta-v3-large-squad2": pipeline("question-answering", model="deepset/deberta-v3-large-squad2", tokenizer="deepset/deberta-v3-large-squad2"),
    "deepset/bert-large-uncased-whole-word-masking-squad2": pipeline("question-answering", model="deepset/bert-large-uncased-whole-word-masking-squad2", tokenizer="deepset/bert-large-uncased-whole-word-masking-squad2"),
    "deepset/roberta-base-squad2": pipeline("question-answering", model="deepset/roberta-base-squad2", tokenizer="deepset/roberta-base-squad2"),
    "microsoft/deberta-large-mnli": pipeline("zero-shot-classification", model="microsoft/deberta-large-mnli"),
    "valhalla/distilbart-mnli-12-1": pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-1")
}

@app.post("/question-answering")
async def question_answering(request: QuestionAnsweringRequest):
    if request.model in models:
        model = models[request.model]
    else:
        return {
            "message": "Error: cannot find model"
        }

    result = model(request.payload.question, request.payload.context)
    return {
        "answer": result["answer"], 
        "score": result["score"]
    }

@app.post("/multiple-choice")
async def multiple_choice(request: MultipleChoiceRequest):
    if request.model in models:
        model = models[request.model]
    else:
        return {
            "message": "Error: cannot find model"
        }

    result = model(request.payload.context, candidate_labels=request.payload.candidate_labels, multi_label=True)
    return {
        "labels": result["labels"],
        "scores": result["scores"]
    }