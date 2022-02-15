# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    answer = []
    
    for char in s:
        if answer and answer[-1] == char:
            answer.pop()
            continue
        answer.append(char)

    return 0 if answer else 1
  
  # 처음에 문자열로 풀다가, 시간 초과가 많이 나서 왜 그럴까 고민했는데
  # 배열로 푸니까 해결되었음 !
