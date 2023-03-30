from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service.FormService import FormService

from dto.FormSubmit import FormSubmit
from models.FormAnswer import FormAnswer

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