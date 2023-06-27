import json
from typing import Annotated
from enums.FieldType import FieldType
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from service.FormService import FormService
from service.FieldService import FieldService
from service.AudioService import AudioService

from dto.FormSubmit import FormSubmit
from models.FormAnswer import FormAnswer
from models.FieldAnswer import FieldAnswer
from dto.FieldSubmit import FieldSubmit
from dto.AudioSubmit import AudioSubmit

import os
from dotenv import load_dotenv
from models.FormItem import FormItem
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

fieldService = FieldService()
formService = FormService()
audioServiceService = AudioService()
# fieldService = None
# formService = None
# audioServiceService = None

@app.get("/")
def default():
    return {
        "hello": "world",
    }

@app.post("/forms")
async def formsSubmit(formSubmit: FormSubmit) -> FormAnswer:
    return formService.fillForm(formSubmit)

@app.post("/speech")
async def convertSpeechToText(audioFile: bytes = File(...), field: str = Form(...), formName: str = Form(...)) -> FieldAnswer:
    field = json.loads(field)
    field = FormItem(**field)
    context = audioServiceService.fillInAudioToText(audioFile)
    field = FieldSubmit(context=context, field=field, formName=formName)
    return await fieldSubmit(field)

@app.post("/testFile")
async def testFile(file: bytes = File(...)) -> str:
    return len(file)

@app.post("/field")
async def fieldSubmit(field: FieldSubmit) -> FieldAnswer:
    return fieldService.fillInField(field.field, field.context)

@app.get("/forms")
async def formsGetAll() -> list:
    return formService\
        .getAllForms()
