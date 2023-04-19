echo Starting Backend
cd Backend\\zenya-form-prototype-backend
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
cd src
python -m uvicorn main:app --reload