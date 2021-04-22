# setrecursionlimit을 하면 recursionlimit 의 수를 정해줄 수 있다!

import sys
sys.setrecursionlimit(300000)
answer = 0
def solution(a, edges):
    if sum(a) != 0:
        return -1
    global answer
    length = len(a)
    graph = [[] for i in range(length)]
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(node, parent):
        global answer
        for point in graph[node]:
            if point != parent:
                dfs(point, node)
        answer += abs(a[node])
        a[parent] += a[node]
        a[node] = 0
    dfs(0, 0)
    return answer
