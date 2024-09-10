def predict():
    #from fishregression.api.lr import lr_api
    #from fishregression.api.knn import knn_api
    import requests as r
    
    your_ec2_ipv4 = input("""물고기 api에 접속할 주소를 입력하세요
(해당 주소에 api가 도커 컨테이너가 실행되어있어야합니다. 포트는 8080):""")
    base_url = f"http://{your_ec2_ipv4}:8080/"
    length = float(input("물고기의 길이를 입력하세요: "))
    length_url = f"{base_url}lr"
    params = {'l': length}
    response = r.get(length_url, params=params)
    print(response.text)
    l = response.json()
    print("*"*100)
    print(response.text)
    print("*"*100)
    ## weight 예측 선형회귀 API 호출
    weight = l.get('weight')
    dydx0 = l.get('dydx0')

    ## 물고기 분류 API 호출
    fish_url = f"{base_url}knn"
    params = {'w': weight, 'l': length, 'dydx0': dydx0}
    response = r.get(fish_url, params=params)
    f = response.json()
    fish_class = f.get('result')

    ## 출력
    print(fish_class)
