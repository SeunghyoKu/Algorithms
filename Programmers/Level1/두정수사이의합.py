#두 정수 사이의 합
#https://programmers.co.kr/learn/courses/30/lessons/12912

#두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
#예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

def adder(a, b):
    sum = 0

    if a < b:
        for i in range (a, b+1):
            sum += i
    else:
        for i in range(b, a+1):
            sum += i

    return sum

#다른 사람의 풀이
#if a > b: a, b = b, a ==> 만약 a>b라면, a,b 가 아니고 b,a
#sum(): 합쳐주는 함수
def adder(a, b):
    if a > b: a, b = b, a
    return sum(range(a,b+1))
