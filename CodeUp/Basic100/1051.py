#두 정수(a, b)를 입력받아, b가 a보다 크거나 같으면 1, b가 a보다 작으면 0을 출력하는 프로그램을 작성해보자.

a, b = input().split(" ")

if int(b)>=int(a):
  print(1)
else:
  print(0)
