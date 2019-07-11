#두 정수 사이의 합
#https://programmers.co.kr/learn/courses/30/lessons/12912

#두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요. 
#예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

#나의 풀이
#조금.. 무식하게 풀었다..!

def solution(a, b):
    sum = 0

    #a보다 b가 클 때는 a에서 b까지의 합 구하기
    if a < b:
        for i in range (a, b+1):
            sum += i
    #b가 a보다 클 때는 b에서 a까지의 합 구하기
    else:
        for i in range(b, a+1):
            sum += i
        
    return sum
    
#다른 사람의 풀이1
#sum을 이용한 풀이
def adder(a, b):
    #a가 b보다 클 때는 순서가 b, a로 바꿔서
    if a > b: a, b = b, a
    return sum(range(a,b+1))


#다른 사람의 풀이2
#min과 max를 이용한 풀이
def adder2(a, b):
    #최솟값과 최댓값으로 풀면 되는 거였다!
    return sum(range(min(a,b),max(a,b)+1))
