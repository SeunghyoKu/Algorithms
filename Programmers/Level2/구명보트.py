# 구명보트 - 그리디
# https://programmers.co.kr/learn/courses/30/lessons/42885

'''
효율성을 넘기는 게 어려웠는데
del 하거나 pop(0)은 n이라 시간이 더 들기 떄문에
인덱스 값을 유지하며 계산하는 것이 더 시간이 적게 든다고 한다
'''

def solution(people, limit):
    people.sort()
    answer = 0
    
    left = 0
    right = len(people) - 1
    while right - left >= 1:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    if left == right:
        answer += 1
    return answer
