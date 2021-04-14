# 생존 신고용
# dfs 문제

answer = 0
def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [False for i in range(len(words))]
    stack = [begin]
    global answer
    DFS(target, stack, words, visited)

    return answer

def count_diff(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return count

def DFS(target, stack, words, visited):     
    global answer
    while stack:
        curr = stack.pop()
        if curr == target:
            return answer
        for i in range(len(words)):
            if count_diff(words[i], curr) != 1:
                continue
            if not visited[i]:
                visited[i] = True
                stack.append(words[i])
        answer += 1
