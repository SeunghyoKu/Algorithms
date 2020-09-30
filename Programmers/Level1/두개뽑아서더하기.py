# 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3

# 문제
'''
정수 배열 numbers가 주어집니다.
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를
배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
'''


# 나의 풀이
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in numbers[i+1:]:
            answer.append(numbers[i]+j)
    return sorted(list(set(answer)))
    
# 뭔가 오랜만에 파이썬을 사용해서 그런지 가독성이 떨어지는 것 같다
# 위에서는 range(len())으로 불러오고 아래에서는 그냥 불러오는 것이 특히 잘못 된 거 같은데
# 이런 부분도 고쳐서 풀 도록 노력해야 겠다.
