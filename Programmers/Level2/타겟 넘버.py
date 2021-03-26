# 타겟 넘버
from collections import deque

def solution(numbers, target):
    arr = [-1, 1]
    queue = deque()
    queue.append((0, 0))
    answer = 0
    
    while queue:
        sum_number, level = queue.popleft()
        if level > len(numbers):
            break
        if level == len(numbers) and sum_number == target:
            answer += 1
            
        for i in range(2):
            dx = numbers[level - 1] * arr[i]
            queue.append((sum_number + dx, level + 1))
    
    return answer
'''
deque로 한 번 풀어봐야지 하고 했던 문제이다.
처음에 sum 합계 값으로만 풀어보려 했는데 그러면 길이를 생각하는 게 어려워져서
변수를 하나 더 써야만 됐다

마지막에 반복문 말고 그냥 더하고 빼는 게 더 좋았을 거 같다
코드가 더 길어지니까
'''

# 다른 사람의 풀이
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
'''
너무 대단한 풀이 아닙니까 이거
solution 함수 자체를 재귀로 두고 푸는 방법이었다
너무..  멋진 풀이다
'''
# 다른 사람의 풀이 2
from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
'''
파이써닉한 코드 같아서 가져왔다.
cartesian product를 표현할 때 쓰는 메소드라고 한다.
이 메소드를 이용하면 두 개 이상의 리스트의 모든 조합을 구할 수 있다고 한다.
그거의 합을 표현한 list s에서 target만 쓰는 방법..
너무.. 멋진 풀이다 2
'''
