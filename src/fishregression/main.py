from typing import Union
from fishregression.api.lr import lr_api
from fishregression.api.knn import knn_api
from fastapi import FastAPI

app = FastAPI()
dydx0 = 0

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/knn")
def read_item(w: float, l: float):
    global dydx0
    fish_class, e = knn_api(l, w, dydx0)
    if e == 0:
        result_msg = f"🐟 길이 {l}에 무게 {w}인 물고기는 {fish_class}로 예측됩니다!"
    else:
        result_msg = f"🐟 길이가 너무 작거나 커서 극값에 해당하는 길이인 {dydx0}에 해당하는 무게는 {round(w-99999.99999, 3)}로 예측되며 물고기의 종류는 {fish_class} 같습니다!"
    return {"result": result_msg}


@app.get("/lr")
def read_item(l: float):
    global dydx0
    weight, dydx0 = lr_api(l)
    return {"weigtbongkim03/fish-lb:0.6.2ht": weight, "dydx0": dydx0}
