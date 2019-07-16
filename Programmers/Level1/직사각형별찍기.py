#직사각형 별찍기
#https://programmers.co.kr/learn/courses/30/lessons/12969?language=python3

#이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
#별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.
#파이썬은 문자를 숫자로 곱하면 반복합니다.

#map(): 입력값 받는다. 반복 가능한 자료형에 대해서 함수를 각각 적용한 결과 (여기선 int 함수를 쓴 것)
#int함수? 그냥 input 값을 int로 받는 것
#strip(): 양쪽 공백 없애기(왼쪽 공백 lstrip(), 오른쪽 공백 rstrip())

a, b = map(int, input().strip().split(' '))
print(('*'*a +'\n')*b)

#다른 사람 풀이
#row만큼 col에 *곱한 것 반복하기
col, row = map(int, input().split())
for i in range(row):
    print('*'*col)

