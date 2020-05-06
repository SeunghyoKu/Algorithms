# 프로그래머스 - 탑
# https://programmers.co.kr/learn/courses/30/lessons/42588/


def solution(heights):
    answer = [0 for i in range(len(heights))]
    for i in range(len(heights)-1,0,-1):
        for j in range(i-1,-1,-1):
            if heights[j] > heights[i]:
                answer[i] = j+1
                break
    return answer
    

'''
range를 뒤에서 부터 잡아서 계산하면 쉬울 거 같아서 -1씩 줄어드는 range를 활용했다.
만약, answer에 수신 받은 탑의 인덱스를 저장하고나면 반복문을 더이상 반복할 필요가 없으므로 break를 이용해빠져나오면 된다.
'''
