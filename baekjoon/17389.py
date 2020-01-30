# 백준 17389번 문제 - 반복문 이용해 푸는 구현 문제
# https://www.acmicpc.net/problem/17389

'''
첫 번째 줄에 OX표의 길이인 자연수 N이 주어진다. (1 ≤ N ≤ 10,000)
두 번째 줄에 OX표를 의미하는 문자열 S가 주어진다. S는 O(알파벳 대문자 O, ASCII 코드 79)와 X(알파벳 대문자 X, ASCII 코드 88)로만 구성되어 있으며, 길이는 N이다.
문자열 S의 i 번째 글자가 O이면 해당 참가자가 i 번째 문제를 맞혔음을 의미하고, X이면 틀렸음을 의미한다.

첫 번째 줄에 입력으로 들어온 OX표의 점수를 출력한다.
'''

# 나의 풀이

N = int(input())
S = input()
bonus = 0
score = 0

for i in range(N):
    # X를 만나면 bonus 초기화
    if S[i] == 'X':
        bonus = 0
    # O를 만나면 score에 보너스와 i+1 점 만큼 추가한 다음, bonus 증가
    else:
        score += (i + 1) + bonus
        bonus += 1
print(score)


# 다른 사람의 풀이

# for i in enumerate(n) -> i는 (index, value)의 튜플 형태로 반환
# for i, v in enumerate(n) -> i는 index, v는 value로 반환
# 튜플 형태의 초기화를 사용하여 코드의 길이를 줄일 수 있다.

N, S = input(), input()
score, bonus = 0,0

for idx, OX in enumerate(S):
    if OX == 'O':
        score, bonus = score + idx + 1 + bonus, bonus + 1
    else:
        bonus = 0
        
print(score)
