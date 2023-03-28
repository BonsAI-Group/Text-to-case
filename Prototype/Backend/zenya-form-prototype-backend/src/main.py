from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .dto.FormSubmit import FormSubmit
from .models.FormAnswer import FormAnswer
from .ml.BasicQA import BasicQA

app = FastAPI()

# CORS
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

qa = BasicQA()

@app.post("/forms")
async def forms(formSubmit: FormSubmit) -> FormAnswer:
    return qa.answer_form(formSubmit.context, formSubmit.form)