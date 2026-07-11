from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"This is Home Page"}

@app.get("/about")
def about():
    return {"message":"This is About Page"}