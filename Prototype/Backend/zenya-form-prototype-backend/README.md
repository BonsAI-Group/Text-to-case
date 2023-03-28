# Automatic form filling prototype - Python FastAPI backend
This is a simple backend for the prototype of the Text-to-case project. It is created using Python [FastAPI](https://fastapi.tiangolo.com/).

## How to install

Start by creating a virtual environment
```bash	
python -m venv venv
```
Then activate it
```bash
venv/Scripts/activate
```

Next, you need to install the necessary dependencies
```bash
pip install -r requirements.txt
```

## How to run

To run the backend, you need to run the following command
```bash
uvicorn src.main:app --reload
```
