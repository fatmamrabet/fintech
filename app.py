from fastapi import FastAPI
from core import add, health_check

app = FastAPI()


@app.get("/health")
def health():
    return health_check()


@app.get("/add")
def api_add(a: float, b: float):
    return {"result": add(a, b)}
