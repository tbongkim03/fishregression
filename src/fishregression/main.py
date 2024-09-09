from typing import Union
from fishregression.api.lr import lr_api
from fishregression.api.knn import knn_api
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/knn")
def read_item(w: float, l: float):
    fish_class = knn_api(l, w)
    result_msg = f"🐟 길이 {l}에 무게 {w}인 물고기는 {fish_class}로 예측됩니다!"
    return {"result": result_msg}


@app.get("/lr")
def read_item(l: float):
    weight = lr_api(l)
    return {"weight": weight}
