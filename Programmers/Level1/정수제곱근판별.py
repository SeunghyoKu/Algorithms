#정수 제곱근 판별
#https://programmers.co.kr/learn/courses/30/lessons/12934

#임의의 정수 n에 대해, n이 어떤 정수 x의 제곱인지 아닌지 판단하려 합니다.
#n이 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

#나의 풀이
def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        if i**2 == n:
            answer = (i+1)**2
            break
    return answer or -1   

#1부터 n까지의 숫자들 중에서, 만약 i 제곱의 숫자가 n이라면 바로 반복문을 끝낸 후, 답을 출력하는 함수
#math를 import해서 sqrt를 써도 됐잖아 ?!? 싶지만 import math 가 안되는줄 알고 이렇게 짰는데 알고보니 된다고 한다.
#제곱근은 **0.5해도 구할 수 있다는 걸 몰랐다.
