echo Starting Backend
cd Backend\\zenya-form-prototype-backend
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
mvn dependency:copy-dependencies -DoutputDirectory=./jars -f %cd%\venv\Lib\site-packages\sutime\pom.xml
cd src
python -m uvicorn main:app --reload
