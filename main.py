from fastapi import FastAPI
from starlette.responses import FileResponse

app = FastAPI()

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.get("/")
def root():
    return {"message": "CI/CD radi!"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

