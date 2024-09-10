def lr_api(length):
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    import pickle
    import os
    from sympy import symbols, diff, solve 

    fish_length = np.array([25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
        31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
        35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
        10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
        )
    fish_weight = np.array([242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
        500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
        700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7,
        7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]
        )

    train_input, test_input, train_target, test_target = train_test_split(fish_length, fish_weight, random_state=42)
    train_input = train_input.reshape(-1,1)
    test_input = test_input.reshape(-1,1)

    train_poly = np.column_stack((train_input ** 2, train_input))
    lr = LinearRegression()
    lr.fit(train_poly, train_target)

    # 다항회귀에서 예측불가능한 극점 반대부분 예외처리

    x = symbols('x')

    A = lr.coef_[0]
    B = lr.coef_[1]
    C = lr.intercept_

    fx = A * x**2 + B * x + C
    dfx = diff(fx, x)
    dydx0 = solve(dfx, x)

    with open("model.pkl", "wb") as f:
        pickle.dump(lr, f)

    with open("model.pkl", "rb") as f:
       fish_lr = pickle.load(f)

    if length > min(train_input) or length < max(train_input):
        lr_w = fish_lr.predict([[length ** 2, length]])
        weight = round(float(lr_w[0]), 3)
    else:
        lr_w = fish_lr.predict([[dydx0 ** 2, length]])
        weight = round(float(lr_w[0]), 3)
    return weight, dydx0
