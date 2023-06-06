from fastapi import FastAPI
from transformers import pipeline
from RequestModels.question_answering_request import QuestionAnsweringRequest
from RequestModels.multiple_choice_request import MultipleChoiceRequest
app = FastAPI()

@app.post("/question-answering")
async def question_answering(request: QuestionAnsweringRequest):
    model = pipeline("question-answering", model=request.model, tokenizer=request.model)
    result = model(request.payload.question, request.payload.context)
    return {
        "answer": result["answer"], 
        "score": result["score"]
    }

@app.post("/multiple-choice")
async def multiple_choice(request: MultipleChoiceRequest):
    model = pipeline("zero-shot-classification", model=request.model)
    result = model(request.payload.context, candidate_labels=request.payload.candidate_labels, multi_label=True)
    return {
        "labels": result["labels"],
        "scores": result["scores"]
    }