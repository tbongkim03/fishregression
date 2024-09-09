from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("knn")
def read_item(w: float, l: float):
    return {"item_id": "todo"}


@app.get("lr")
def read_item(l: float):
    return {"item_id": "todo"}
