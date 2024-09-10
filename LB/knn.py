def knn_api(length, weighti, dydx0):
    import numpy as np
    from sklearn.neighbors import KNeighborsClassifier
    import pickle
    import os
    
    fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
            31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
            35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
            10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
    fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
            500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7,
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

    fish_data = np.column_stack((fish_length, fish_weight))
    test_data = np.column_stack(([1,2,3],[10,20,30]))
    fish_target = np.concatenate((np.ones(35), np.zeros(14)))
    kn = KNeighborsClassifier(n_neighbors=5)
    kn.fit(fish_data, fish_target)

    with open("model.pkl", "wb") as f:
        pickle.dump(kn, f)

    with open("model.pkl", "rb") as f:
        fish_knn = pickle.load(f)
    
    e=0
    # 예외처리 확인
    if weight > 99999:
        weight = weight - 99999.99999
        
        e = 1
        
    knn_p = fish_knn.predict([[dydx0,weight]])
    fish_type = "빙어"
    if int(knn_p[0]) == 1:
        fish_type = "도미"
    return fish_type, e
