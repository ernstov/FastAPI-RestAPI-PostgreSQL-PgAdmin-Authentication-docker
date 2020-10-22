### Install the dependencies
```sh
pip install -r requirements.txt
```

### API - v0
 - Navigate to `backend` folder and run below command to start the API
 - `v0` Code located at `backend/app/api`
```sh
uvicorn app.api.main:app --reload --workers 1 --host 0.0.0.0 --port 8989
```
Open http://0.0.0.0:8989/docs to access the API docs
<br>

### API - v1
 - Navigate to `backend` folder and run below command to start the API
 - `v1` Code located at `backend/app/api_v1`
```sh
uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8900
```
Open http://0.0.0.0:8900/docs to access the API docs
<br>