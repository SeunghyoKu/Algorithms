#두 가지의 참(1) 또는 거짓(0)이 입력될 때, 모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.

a, b = input().split(" ")
a = bool(int(a))
b = bool(int(b))


if a == False and b == False:
  print(1)
else:
  print(0)
  
#c = int(a == False and b == False)
#print(c)
#두가지 방법으로 풀어보았다.
