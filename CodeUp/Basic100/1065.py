#세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.

a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

if a%2 == 0:
  print(a)

if b%2 == 0:
  print(b)

if c%2 == 0:
  print(c)
