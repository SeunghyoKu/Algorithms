#x만큼 간격이 있는 n개의 숫자
#https://programmers.co.kr/learn/courses/30/lessons/12954

#함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.\
#다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

#나의 풀이
def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)   
    return answer

#answer라는 리스트에 1부터 n+1까지의 숫자들을 곱한 값들을 append하는 식으로 만들었습니다.
