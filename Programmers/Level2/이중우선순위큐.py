# 이중우선순위 큐
# Heap
# https://programmers.co.kr/learn/courses/30/lessons/42628

from collections import deque

def solution(operations):
    answer = [0, 0]
    queue = deque([])
    
    for op in operations:
        com, num = op.split(" ")
        if com == "I":
            queue.append(int(num))
            queue = deque(sorted(queue))
        if com == "D" and len(queue) > 0:
            if num == "1":
                queue.pop()
            else:
                queue.popleft()
    if len(queue) == 0: return answer
    return [queue[-1], queue[0]]
  
'''
힙큐 문제인데 그냥 큐로 풀었는데 시간 초과가 안났다 ㅋㅋ
오랜만에 파이썬 봐서 까먹었는데 if not queue 같은 표현이 더 가독성이 좋았을 것 같다

힙은 max heap과 min heap이 있으며, max heap은 부모노드의 키 값이 자식 노드의 키 값보다 항상 크다.
min heap과 반대로 부모 노드의 키 값이 자식 노드의 키 값보다 항상 작다.

그래서, 따로 정렬 작업이 없더라도 제대로 동작한다.
'''

# 힙을 이용해 풀은 다른 분의 풀이
import heapq

def solution(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]
  
'''

'''
