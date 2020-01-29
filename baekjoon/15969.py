# 백준 15969 행복 문제
# https://acmicpc.net/problem/15969

'''
표준 입력으로 다음 정보가 주어진다. 첫 번째 줄에는 학생 수 N이 주어진다. 다음 줄에는 N명의 학생 점수가 공백 하나를 사이에 두고 주어진다.
표준 출력으로 가장 높은 점수와 가장 낮은 점수의 차이를 출력한다.
'''

N = int(input())
student = list(map(int, input().split())) 
print(max(student) - min(student))

# list의 형태에서 min 과 max 함수를 사용할 수 있기에 리스트로 감싸줬다.
# [map(int, input().split())] 도 같은 표현으로 사용될 수 있다.
