# https://programmers.co.kr/learn/courses/30/lessons/42747#
# 나의 풀이
def solution(citations):
    h_index = 0
    
    if len(citations) == 1:
        return 0 if citations[0] == 0 else 1
    
    for i in range(1, len(citations) + 1):
        count = 0
        for citation in citations:
            if citation - i < 0:
                continue
            count += 1
            if count == i:
                h_index = i
                break

    return h_index
  
  
# 다른 사람의 풀이
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    
    # l-i : i인덱스 값과 같거나 큰 수의 개수
    # 역으로 큰 거부터 계산해서 
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
