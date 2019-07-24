#하샤드 수
#https://programmers.co.kr/learn/courses/30/lessons/12947?language=python3

#양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
#예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
#자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

#나의 풀이
def solution(x):
    sum = 0
    for i in range(len(str(x))):
        sum += int(str(x)[i])
    return x%sum == 0
#sum 이라는 변수에, 자릿수의 합을 넣어주는 식으로 풀었습니다.

#다른 사람의 풀이
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0

#sum()함수를 활용하여 더 간결한 풀이를 한 것을 알 수 있다.
#어떻게 변수명을 sum 이라고 지으면서 sum()을 기억하지 못했는지.. 조금 아쉽다. 
