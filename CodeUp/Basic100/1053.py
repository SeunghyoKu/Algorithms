#1(true, 참) 또는 0(false, 거짓) 이 입력되었을 때 반대로 출력하는 프로그램을 작성해보자.

bool = int(input())

if bool == 1:
  print(0)
elif bool == 0:
  print(1)
  

'''
다른 풀이
  
a=input()

x=int(a)
b=bool(x)
x=int(not b)

print(x)

bool(): 파이썬 내장함수, 참과 거짓을 식별한다.
not b: 논리 상태를 반전시킨다.
int(not b): 반전시킨 논리 상태를 정수 값(0 또는 1)로 변환하여 보여준다.
'''
