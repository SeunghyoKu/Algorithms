#문자열 내 마음대로 정렬하기
#https://programmers.co.kr/learn/courses/30/lessons/12915

#문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다.
# 예를 들어 strings가 [sun, bed, car]이고 n이 1이면 각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬합니다.

#나의 풀이
def solution(strings, n):
    for i in range(len(strings)):
        #그냥 n번째 거 맨 앞에 붙여서 정렬 하면 되는 거 아녀?
        strings[i] = strings[i][n] + strings[i]

    strings.sort()

    #출력할 때 [1:]로 하면 첫번째 글자는 빼고 출력한다.
    for i in range(len(strings)):
        strings[i] = strings[i][1:]

    return strings

#다른 사람의 풀이
def strange_sort(strings, n):
    return sorted(strings, key=lambda x: x[n])

#lambda 는 무엇일까? 파이썬 공식문서 https://docs.python.org/3/howto/sorting.html
#사용하는 방법
#sort(key = lambda x: x[n]) : x중에서 n번째 것을 비교한다.
