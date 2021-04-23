# https://programmers.co.kr/learn/courses/30/lessons/43105
# 정수 삼각형: DP 문제

def solution(triangle):
    length = len(triangle)
    maps = [[0 for j in range(len(triangle[i]))] for i in range(length)]
    maps[length - 1] = triangle[length - 1]
    
    for i in range(length - 2, -1, -1):
        for j in range(i + 1):
            maps[i][j] = max(maps[i + 1][j], maps[i + 1][j + 1]) + triangle[i][j]
            
    return maps[0][0]
