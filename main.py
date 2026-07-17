from fastapi import FastAPI

app = FastAPI()

tasks = [
    {
        "id":1,
        "title":"Learning FastAPI",
        "done":True
    },
    {
        "id":2,
        "title":"Doing Leetcode problems",
        "done":True
    },
    {
        "id":3,
        "title":"Notes Making",
        "done":False
    }
]

def findtask(id):
    for i in tasks:
        if i["id"] == id:
            return i

@app.get("/")
def hello():
    return {"message":"Hello Server"}

@app.get("/")
def root():
    return {
        "name":"Task API",
        "version":"1.0",
        "endpoints":[
            "/tasks"
        ]
    }

@app.get("/health")
def health():
    return {"status":"ok"}

@app.get("/tasks")
def task():
    return {"data":tasks}

@app.get("/tasks/{id}")
def taskById(id):
    task = findtask(int(id))
    return {"data":task}