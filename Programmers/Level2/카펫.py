# 카펫 - 완전탐색
# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    aliquots = []
    for i in range(3, total):
        if total % i == 0:
            aliquots.append(i)
    for aliquot in aliquots:
        if (aliquot - 2) * (total / aliquot - 2) == yellow:
            return sorted([aliquot, total / aliquot], reverse=True)
    return False
