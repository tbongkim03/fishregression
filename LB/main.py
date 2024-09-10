from typing import Union
from fishregression.api.lr import lr_api
from fishregression.api.knn import knn_api
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/knn")
def read_item(w: float, l: float, dydx0: float):
    fish_class, e = knn_api(l, w, dydx0)
    if e == 0:
        result_msg = f"🐟 길이 {l}에 무게 {w}인 물고기는 {fish_class}로 예측됩니다!"
    else:
        result_msg = f"🐟 길이가 너무 작거나 커서 극값에 해당하는 길이인 {l}에 해당하는 무게는 {w}로 예측되며 물고기의 종류는 {fish_class} 같습니다!"
    return {"result": result_msg}


@app.get("/lr")
def read_item(l: float):
    weight, dydx0 = lr_api(l)
    return {"weight": weight, "dydx0": dydx0}
