#두 정수(a, b)를 입력받아 a와 b가 서로 다르면 1, a와 b가 같으면 0을 출력하는 프로그램을 작성해보자.

a, b = input().split(" ")
if int(a) == int(b):
  print(0)
else:
  print(1)
