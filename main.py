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
        
def find_task_index(id):
    for index, task in enumerate(tasks):
        if task["id"] == id:
            return index

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

@app.put("/tasks/{id}")
def update_task(id: int, response: Response,updated_task: dict = Body(...)):

    task = findtask(id)

    if not task:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Task {id} not found"}

    if "title" not in updated_task or updated_task["title"].strip() == "":
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Title is required"}

    task["title"] = updated_task["title"]

    if "done" in updated_task:
        task["done"] = updated_task["done"]

    return {"data": task}

@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int, response: Response):

    index = find_task_index(id)

    if index is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Task {id} not found"}

    tasks.pop(index)

    return 