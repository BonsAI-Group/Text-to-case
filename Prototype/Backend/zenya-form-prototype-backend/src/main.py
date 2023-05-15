from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from service.FormService import FormService
from service.FieldService import FieldService

from dto.FormSubmit import FormSubmit
from models.FormAnswer import FormAnswer
from models.FieldAnswer import FieldAnswer
from dto.FieldSubmit import FieldSubmit

import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# CORS
origins = [
    os.environ.get("FRONTEND_URL")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/forms")
async def formsSubmit(formSubmit: FormSubmit) -> FormAnswer:
    return FormService(formSubmit.form.name).fillForm(formSubmit)

@app.post("/field")
async def fieldSubmit(field: FieldSubmit) -> FieldAnswer:
    return FieldService(field.formName).fillInField(field.field, field.context)

@app.get("/forms")
async def formsGetAll() -> list:
    # This empty string is a hack because of a bad design of the FormService class.
    return FormService("")\
        .getAllForms()
