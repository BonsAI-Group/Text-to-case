from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from service.FormService import FormService
from service.FieldService import FieldService
from service.SpeechToTextService import SpeechToTextService

from dto.FormSubmit import FormSubmit
from models.FormAnswer import FormAnswer
from models.FieldAnswer import FieldAnswer
from dto.FieldSubmit import FieldSubmit
from dto.AudioSubmit import AudioSubmit

import os
from dotenv import load_dotenv

from ml.BertLargeSingleModelQuestionAnswerer import BertLargeSingleModelQuestionAnswerer
from ml.DateTimeConverter import DateTimeConverter
from ml.DestilbertBaseUncasedMnli import DestilbertBaseSingleModelMultiChoice
from ml.MultiModelQuestionAnswerer import MultiModelQuestionAnswerer
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
speechToTextServiceService = SpeechToTextService()

@app.post("/forms")
async def formsSubmit(formSubmit: FormSubmit) -> FormAnswer:
    return formService.fillForm(formSubmit)

@app.post("/speech")
async def convertSpeechToText(audio_file : AudioSubmit) -> str:
    return speechToTextServiceService.fillInSpeechToText(audio_file)

@app.post("/field")
async def fieldSubmit(field: FieldSubmit) -> FieldAnswer:
    return fieldService.fillInField(field.field, field.context)

@app.get("/forms")
async def formsGetAll() -> list:
    return formService\
        .getAllForms()
