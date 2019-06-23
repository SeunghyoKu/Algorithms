#두 가지의 참(1) 또는 거짓(0)이 입력될 때, 모두 참일 때에만 참이 계산되는 프로그램을 작성해보자.
#파이썬의 조건문에서 여러가지 조건이 있을때 and 를 사용한다.

bool1, bool2 = input().split(" ")

bool1 = int(bool1)
bool2 = int(bool2)

if bool1 == 1 and bool2 == 1:
  print(1)
else:
  print(0)
  
'''
모범답안

a,b=input().split()

x=int(a)
y=int(b)
b1=bool(x)
b2=bool(y)
z=int(b1 and b2)

print(z)


'''
