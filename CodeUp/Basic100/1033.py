#10진수를 입력받아 16진수(hexadecimal)로 출력하는 프로그램을 작성해보자.

#이 전 문제랑 뭐가 다른 거지..?
#라고 생각했는데 hex로 변경한 후 대문자로 출력하는 문제였다.
#upper()를 사용하면 대문자로 변경이 가능하다.
num = int(input())
hexa = hex(num)[2:]
print(str(hexa).upper())

'''
다른 사람의 풀이!!

a=input()
n=int(a)
print('%X' % n)

%X의 형태를 정해주면, 대문자로 입력 받을 수 있다.
%x는 원래 16진수의 형태이다.
%o는 8진수의 형태이다.


... 이게 더 간단한 방법인 듯 하다.
'''
