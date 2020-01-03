# 문제 링크: https://www.acmicpc.net/problem/10828

# 스택 구조를 직접 만들어서 실습해볼 수 있는 문제
# 그냥 함수 형태로 만들어서 풀었다.

import sys

num = int(input())
read = sys.stdin.readline
stack = []

def push(data):
    stack.append(data)

def pop():
    if len(stack) == 0:
        return -1
    else:
        popped = stack[-1]
        del stack[-1]
        return popped

def size():
    return len(stack)

def empty():
    return 1 if len(stack) == 0 else 0

def top():
    return stack[-1] if len(stack) != 0 else -1

for i in range(num):
    commands = read().split()
    com = commands[0]
    if com == 'push':
        push(int(commands[1]))
    elif com == 'pop':
        print(pop())
    elif com == 'size':
        print(size())
    elif com == 'empty':
        print(empty())
    elif com == 'top':
        print(top())
 
 # 계속 시간 초과가 떠서 맘고생을 했는데 input() 함수가 입력 받는 수가 많아지면 시간이 매우 느려지기 때문에
 # sys를 import 하여 sys.stdin.readline를 사용하면, 입출력 시간이 줄어들기 때문에
 # 해당 문제의 제한 시간을 넘길 수 있는 것으로 보입니다.
