# Task API

A simple CRUD API built using FastAPI.

## Installation

pip install -r requirements.txt

## Run

uvicorn main:app --reload

## Endpoints

| Method | Endpoint |
|--------|----------|
| GET | / |
| GET | /health |
| GET | /tasks |
| GET | /tasks/{id} |
| POST | /tasks |
| PUT | /tasks/{id} |
| DELETE | /tasks/{id} |

## Sample curl Output

```bash
curl -i http://127.0.0.1:8000/tasks
```
Output:
```HTTP/1.1 200 OK
date: Sat, 18 Jul 2026 05:35:57 GMT
server: uvicorn
content-length: 158
content-type: application/json

{"data":[{"id":1,"title":"Learning FastAPI","done":true},{"id":2,"title":"Doing Leetcode problems","done":true},{"id":3,"title":"Notes Making","done":false}]}(venv) 
```

## Swagger UI Screenshot

![Swagger UI](screenshots/swagger.png)