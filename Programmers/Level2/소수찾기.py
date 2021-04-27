# 소수 찾기 - 완전탐색
# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations
import math

def solution(numbers):
    numbers = list(numbers)
    answer = []
    for i in range(1, len(numbers) + 1):
        combs = list(map(int, map(''.join, permutations(numbers, i))))
        for num in combs:
            if is_prime(num):
                answer.append(num)
    return len(list(set(answer)))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
