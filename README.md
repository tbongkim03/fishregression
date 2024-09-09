# fishregression

## 0.1.0 환경세팅
- python 3.11.9
- dependencies : scikit-learn, "uvicorn[standard]"
- note dG : notebook, matplotlib
- test dG : pytest, pytest-cov

- [x] fishregression 프로젝트 만들기
- [x] 이전 프로젝트 참조하여 pdm add 하기
- [x] run jupyter notebook OR vscode ipynb 확장자 파일 만들어 열어 보고 구동 확인
- [x] github push

![image](https://github.com/user-attachments/assets/11b79446-af3f-469f-914d-0f434a52d597)


## 0.2.0 reg
- test.ipynb 에서
- 회귀분석 연습
- numpy, matplotlib을 이용하여 기존 물고기 길이, 무게 정보 시각화
- KNR(KNeighborsRegressor, K-최근접 이웃 회귀)을 통해 길이가 주어졌을 때 무게 예측
- 발생한 문제점
```python
ValueError: Expected 2D array, got 1D array instead:
```
- 해결방안
`reshape` 메서드 사용. 인자 reshape(행의 수, 열의 수)
2차원 배열로 만들기 위해 reshape(-1,1) 사용.

- 궁금증
-1은 행의 수가 -1개라는 건가? 무슨의미?
답 : 남은 배열의 길이와 남은 차원으로부터 추정해서 알아서 행을 지정 [출처](https://yololife-sy.medium.com/python-reshape-1-1-%EC%97%90%EC%84%9C-1%EC%9D%98-%EC%9D%98%EB%AF%B8-97b713be5230)

![image](https://github.com/user-attachments/assets/82dfc98d-a8aa-4a25-985e-3ab0e54b1f17)


- 알게된 KNR의 문제점

길이 데이터를 기반으로 무게 예측하는 방법이 k값 근처 데이터틀의 평균값으로 예측함.
따라서 미리 준비된 데이터의 범위와 상당히 떨어져 있으면 일정 길이(수치) 이상부터는 모두 같은 무게로 귀결됨.

```python
43
[[1033.33333333]]
44
[[1033.33333333]]
45
[[1033.33333333]]
46
[[1033.33333333]]
47
[[1033.33333333]]
48
[[1033.33333333]]
49
[[1033.33333333]]
50
[[1033.33333333]]
```

### 0.3.0 linear
- linear regression
- import
```python
from sklearn.linear_model import LinearRegression
```

- how to
```python
#X는 2차원 배열 train_input
#y는 배열 train_target
reg = LinearRegression().fit(X, y)
```

- 직선의 방정식
y = A(기울기 = 계수) * X(값 = 여기서는 생선의 길이) + B(y 절편)

```python
A = reg.coef_ # 계수
B = reg.intercept_ #y 절편, 독립항
```
- 직선 그래프에 나타내기
```python
plt.plot(<[시작할X, 마지막X]>, <[시작할y, 마지막y]>, linewidth=3)
```
![image](https://github.com/user-attachments/assets/8fe11066-ca3c-4fe7-9098-2dd6848b58c5)

- 문제점 X, y 범위 지정하기 어려움

해결방법 : 시작할 점 == 최소값 min(), 마지막 점 == 최대값 max()
![image](https://github.com/user-attachments/assets/b4b485f6-19f2-4367-84b3-fc414e03925c)

### 0.4.0 poly
- poly regression
- 다항식 : weight = A * (length)^2 + B * length + C
- A, B, C ?
```python
A = lr.coef_[0]
B = lr.coef_[1]
C = lr.intercept_
```
- 곡선 그래프에 나타내기
- **sol1**
```python
points = np.arange(0,51)
plt.plot(points, (A * points**2) + (B * points) + C, color="red")
```
![image](https://github.com/user-attachments/assets/62e0e918-5898-4ec1-b6be-3a53281d59af)

- **sol2**
```python
x_values = np.linspace(min(train_input), max(train_input), 100)
y_values = A * x_values ** 2 + B * x_values + C
plt.plot(x_values, y_values, color='red')
```
![image](https://github.com/user-attachments/assets/e995551b-482f-493a-be7f-7eb0064ddd43)

- 문제점 

sol1에서 np.arange(x_0, x_1)을 이용하여 범위를 지정할 경우
데이터에 존재하는 최소값을 지나쳐서 반대쪽도 선이 그어지기 때문에 문제 발생

