#완주하지 못한 선수
#https://programmers.co.kr/learn/courses/30/lessons/42576

#수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
#마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
#완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

#나의 풀이 (시간 초과 풀이)

def solution(participant, completion):
    for i in range(len(participant)):
        if participant.count(participant[i]) - completion.count(participant[i]) == 1:
            return participant[i]
            
#효율성은 안녕..! 하지만 생각나는 대로 쳤던 코드
#결과는 잘 출력되지만.. 시간이 초과해서 다시 코드를 생각했다.

#문제의 카테고리는 '해시'였고, 해시와 관련한 카운트를 해주는 함수가 있는지 찾아보았다.
#https://docs.python.org/2/library/collections.html#collections.Counter


#collection의 Counter를 알게 되었다.
from collections import Counter

def solution(participant, completion):
    participant.sort()
    completion.sort() 
    return list(Counter(participant) - Counter(completion))[0]

#전에 공부한 것에서, 파이썬의 딕셔너리는 차집합, 교집합, 합집합 등의 연산이 가능해서 간단히 차집합을 이용해 풀어주었다.


#다른 사람의 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]


#정렬 후, completion 과 participant의 같은 index값이 다르면, 그것을 리턴하거나 그렇지 않다면 정렬후 남은 마지막 것을 리턴해주는 코드
#정렬을 하면 participant와 completion은 한 개의 값만 다르기 때문에, 굳이 나처럼 비효율적인 count 사용 보다는 훨씬 좋았던 코드
#내가 생각을 좀만 더 했으면 좋았을텐데 하고 아쉬움이 남았다.
    
    
#다른 사람의 풀이2
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]
    
    
#zip():동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
#1번 풀이와 2번 풀이는 비슷한 것 같다. zip을 이용해서 풀어준 것 분. 다 좋은 풀이 같다.
