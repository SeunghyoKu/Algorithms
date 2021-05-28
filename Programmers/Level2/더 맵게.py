import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)   
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        min_1 = heapq.heappop(scoville)
        min_2 = heapq.heappop(scoville)
        scoville.append(min_1 + (min_2 * 2))
        answer += 1

    return answer
