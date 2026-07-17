from fastapi import FastAPI,Response,status,Body

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
def root():
    return {
        "name":"Task API",
        "version":"1.0",
        "endpoints":[
            "/tasks"
        ]
    }


@app.get("/hello")
def hello():
    return {"message":"Hello Server"}

@app.get("/health")
def health():
    return {"status":"ok"}

@app.get("/tasks")
def get_task():
    return {"data":tasks}

@app.get("/tasks/{id}")
def get_task_By_Id(id:int,response:Response):
    task = findtask(id)
    if not task:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error":f"Task {id} not found"}
    return {"data":task}

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: dict = Body(...)):
    
    if "title" not in task or task["title"].strip() == "":
        return Response(
            content='{"error":"Title is required"}',
            media_type="application/json",
            status_code=status.HTTP_400_BAD_REQUEST
        )

    new_task = {
        "id": tasks[-1]["id"] + 1,
        "title": task["title"],
        "done": False
    }

    tasks.append(new_task)

    return {"data": new_task}