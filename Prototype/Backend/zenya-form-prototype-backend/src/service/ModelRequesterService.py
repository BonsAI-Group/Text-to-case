import requests
from typing import List
import os
from dotenv import load_dotenv
load_dotenv()

class ModelRequesterService:
    @staticmethod
    def RequestQuestionAnswering(model: str, question: str, context: str):
        print(f"request => model: {model}, question: {question}, context: {context}")
        response = requests.post(
            f"{os.environ.get('MODEL_URL')}/question-answering", 
            json= {
                "model": model,
                "payload":{
                    "context": context,
                    "question":question
                }
            }
        )
        print(f"result: {response.status_code} =========================================================================")
        response = response.json();
        return response["answer"], response["score"]

    @staticmethod
    def RequestMultipleChoice(model: str, candidate_labels: List[str], context: str):
        response = requests.post(
            f"{os.environ.get('MODEL_URL')}/multiple-choice",
            json= {
                "model": model,
                "payload": {
                    "context": context,
                    "candidate_labels": candidate_labels
                }

            }
        )
        return response.json()
