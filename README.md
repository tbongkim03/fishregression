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
