# Automatic form filling prototype - Python FastAPI backend
This is a simple backend for the prototype of the Text-to-case project. It is created using Python [FastAPI](https://fastapi.tiangolo.com/).

## How to run
To run, first make sure you have all needed dependencies. 

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

Finally, you can run the server
```bash
uvicorn src.main:app --reload
```
