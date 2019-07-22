#최대공약수와 최대공배수
#https://programmers.co.kr/learn/courses/30/lessons/12940

#두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
#배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
#예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

#나의 풀이
def solution(n, m):
    minimum, maximum = 0, 0
    list = []
    
    if n > m:
        n, m = m, n
    
    for i in range(1, n+1):
        if m%i == 0 and n%i == 0:
            list.append(i)
        
    return [max(list),n*m/max(list)]
#그냥 생각할 수 있는 그대로 짰다.
#만약 m과 n이 나누어지는 공통된 숫자가 있다면? ==> list에 append 후, max함수를 이용해 최대의 값을 찾아주었다.
#최소공배수는 두 수를 곱한 후 최대공약수로 나누면 된다. (초등학생때 배웠던 것 같기도 하다.)


#다른 사람의 풀이
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer
    
#유클리드 호제법을 이용한 풀이!
#유클리드 호제법이란: 두 수가 서로(互) 상대방 수를 나누어(除)서 결국 원하는 수를 얻는 알고리즘 (위키피디아)
#2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
#이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때
#나누는 수가 a와 b의 최대공약수이다. 
