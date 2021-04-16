# 괄호 회전하기
# 어제 문제를 잘못 읽어서 못 맞춘 ㅋㅋ 비운의 문제..

def solution(s):
    answer = 0
    for i in range(len(s)):
        s = s[1:] + s[0]
        if search(s):
            answer += 1

    return answer

def search(s):
    start = ['[', '(', '{']
    end = [']', ')', '}']
    stack = []

    if len(s) % 2 == 1:
        return 0

    for ch in s:
        if ch in start:
            stack.append((ch, start.index(ch)))
        if ch in end:
            if len(stack) == 0:
                return False
            if stack[-1][1] == end.index(ch):
                stack.pop()
            else:
                return False
    return True
