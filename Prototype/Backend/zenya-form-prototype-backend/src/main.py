from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service.FormService import FormService
from service.FieldService import FieldService

from dto.FormSubmit import FormSubmit
from models.FormAnswer import FormAnswer
from models.FieldAnswer import FieldAnswer
from dto.FieldSubmit import FieldSubmit

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

@app.post("/forms")
async def forms(formSubmit: FormSubmit) -> FormAnswer:
    return FormService().fillForm(formSubmit)

@app.post("/field")
async def field(field: FieldSubmit) -> FieldAnswer:
    return FieldService().fillInField(field.field, field.context)
