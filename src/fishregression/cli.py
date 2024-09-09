def predict():
    from fishregression.api.lr import lr_api
    from fishregression.api.knn import knn_api
    length = float(input("물고기의 길이를 입력하세요: "))

    ## weight 예측 선형회귀 API 호출
    weight = lr_api(length)

    ## 물고기 분류 API 호출
    fish_class = knn_api(length, weight)

    ## 출력
    print(f"🐟 길이 {length}에 무게 {weight}인 물고기는 {fish_class}로 예측됩니다!")

