# Automatic form filling prototype - Python FastAPI backend
This is a simple backend for the prototype of the Text-to-case project. It is created using Python [FastAPI](https://fastapi.tiangolo.com/).

## Prerequisites
- Python 3.9 or higher 
- [Maven](https://maven.apache.org/) (for installing java libraries)
- [ffmpeg](https://bobbyhadz.com/blog/ffmpeg-is-not-recognized-as-internal-or-external-command) (for converting webm to wav file)

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

Next, you need to install some java libraries. Do this by executing this command.
On windows:
```bash	
mvn dependency:copy-dependencies -DoutputDirectory=./jars -f %cd%\venv\Lib\site-packages\sutime\pom.xml
```	
or this command on linux:
```bash
mvn dependency:copy-dependencies -DoutputDirectory=./jars -f $(python3 -c 'import importlib; import pathlib; print(pathlib.Path(importlib.util.find_spec("sutime").origin).parent / "pom.xml")')
```

## How to run

To run the backend, you need to run the following command **while in the 'src' folder**:
```bash
uvicorn main:app --reload
```
