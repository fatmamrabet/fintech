from fastapi import FastAPI
from core import format_currency, add


app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/format-currency")
def api_format_currency(amount: float):
    return {"result": format_currency(amount)}


@app.get("/add")
def api_add(a: float, b: float):
    return {"result": add(a, b)}
