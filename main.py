from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "CI/CD radi!"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

