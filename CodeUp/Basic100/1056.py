#두 가지의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 다를 때에만 참이 계산되는 프로그램을 작성해보자.

#이러한 논리 연산을 XOR(exclusive or, 배타적 논리합)연산이라고도 부른다. 

#집합의 의미로는 합집합에서 교집합을 뺀 것을 의미한다. 모두 같은 의미이다.

#참/거짓이 서로 다를 때에만 1을 출력하고 이외의 경우에는 0을 출력한다.

a, b = input().split(" ")
a = int(a)
b = int(b)

if a != b:
  print(1)
else:
  print(0)
  
'''
모범 답안

a,b=input().split()

x=int(a)
y=int(b)
b1=bool(x)
b2=bool(y)

z=int((b1==True and b2==False) or (b1==False and b2==True))

print(z)
bool() 함수를 이용, 서로 다른 것 이 트 
'''
