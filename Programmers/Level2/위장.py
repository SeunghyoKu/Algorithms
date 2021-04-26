# 위장 - 해시
# https://programmers.co.kr/learn/courses/30/lessons/42578

from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(list)
    for cloth in clothes:
        clothes_dict[cloth[1]].append(cloth[0])
    answer = 1

    for i in clothes_dict.keys():
        answer *= (len(clothes_dict[i]) + 1)
            
    return answer - 1

'''
이 문제 개인적으로 너무 변태같다
옷을 왜 안입어
선글라스만 쓰는 날은 옷을 다 벗는 걸까?

하지만 선글라스만 쓰더라도 하나는 무조건 걸쳐야 되기 때문에 -1 이다.
경우의 수를 구할 때는 + 1 해서 안입을 때 경우까지 고려해서 해주면 된다.

이렇게 굳이 value 값을 기억할 필요가 없다면
아예 value 값 대신 count 해주면 좋을 것 같다
'''
