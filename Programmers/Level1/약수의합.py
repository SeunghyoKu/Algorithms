#약수의 합
#https://programmers.co.kr/learn/courses/30/lessons/12928
#자연수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.


#나의 풀이
def solution(n):
    sum = 0
    
    for i in range(n+1):
        if i > 0:
            if n%i == 0:
                sum += i
    
    return sum
    
#음. range(1, n+1)로 쓰는 게 더 좋았을 듯 싶다.
#단순하게 나머지가 0, 즉 나누어질 때 sum 에다가 더해주고 출력하는 식으로 짰다.


#다른 사람의 풀이
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

#맞다. 생각해보면 절반 이후의 수들은 따로 계산할 필요가 없는 것이 맞는 것 같다.
#한 문장에 긴 연사자들을 넣는 코드를 짜는 것은 아직 어려운 것 같다.
#주어진 숫자도 약수에 포함되니 주어진 숫자, 그리고 그것의 절반 중에서 나머지가 0인 것들을 더한 값을 반환한다.
