#두 정수(a, b)를 입력받아 a가 b보다 크면 1, a가 b와 같거나 b가 a보다 크다면 0을 출력하는 프로그램을 작성해보자.

a, b = input().split(" ")
a = int(a)
b = int(b)

if a>b:
  print(1)
else:
  print(0)
