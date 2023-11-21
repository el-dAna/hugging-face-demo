from typing import Union
from fastapi import FastAPI
from functions import add

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/add/{a}/{b}")
def add_numbers(a: int, b: int):
    return {f"Addition of {a} and {b} gives": add(a, b)}
