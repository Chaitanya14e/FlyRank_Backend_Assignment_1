from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message":"Hello Server"}

@app.get("/about")
def about():
    return {"message":"This is About Page"}