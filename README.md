# Text-to-case

## Introduction
The goal of this project is to get spoken text from a `speech to text` model, and extract the right information from it to fill in a form.<br>

### Docker
To run the solution in docker
1. Go to the prototype folder
2. Run:
```bash
cd backend/zenya-form-prototype-backend
docker build -t infoland/backend .
docker run -d -e FRONTEND_URL=http://localhost:80 -e MODEL_URL=http://localhost:8001 -p 8000:8000 infoland/backend

cd ../../frontend
docker build -t infoland/frontend .
docker run -d -e REACT_APP_API_URL=http://localhost:8000 -p 80:80 infoland/frontend

cd ../models
docker build -t infoland/models .
docker run -d -p 8001:8000 infoland/models
```
