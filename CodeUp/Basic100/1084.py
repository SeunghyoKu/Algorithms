#빨강(red), 녹색(green), 파랑(blue) 물감을 섞어 여러 가지 물감을 만들어 내려고한다.
#빨강(r), 녹색(g), 파랑(b) 물감의 종류(농도에 따라 0~ n-1 까지 n가지의 농도를 만들 수 있다.)가 주어질 때, 주어진 물감들을 농도를 다르게 섞어 만들 수 있는 모든 물감의 정보(r g b)와 그 최대 개수를 계산해보자.
#빨녹파(r, g, b) 각 물감의 종류(농도) 개수가 공백을 사이에 두고 입력된다. (0 ~ 128)
#예를 들어 3 3 3 은 각 색에 대해서 0~2까지 3가지 물감이 있음을 의미한다.

r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
sum = 0

for i in range(r):
  for ii in range(g):
    for iii in range(b):
      print(i, ii, iii)
      sum += 1
print(sum)
