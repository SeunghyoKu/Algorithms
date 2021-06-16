import math

def solution(n, words):
    mentioned_words = []
    count = 0
    
    for i in range(len(words)):
        if words[i] in mentioned_words:
            return [i % n + 1, math.ceil((i + 1) / n)]
        if i >= 1 and words[i][0] != words[i-1][-1]:
            return [i % n + 1, math.ceil((i + 1) / n)]
        else:
            mentioned_words.append(words[i])
    return [0, 0]
