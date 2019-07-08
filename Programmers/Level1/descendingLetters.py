#문자열 내림차순
#https://programmers.co.kr/learn/courses/30/lessons/12917

#문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
#s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

def solution(s):
    sortedS = sorted(s)
    a = sortedS.reverse()
    return "".join(sortedS)
    
#나의 풀이
#sort하고, reverse하고, 그 다음에 join을 이용하여 리스트를 문자열로 출력해주었다.
#sorted와 reverse를 따로 쓴 것은 sorted sort, 그리고 reverse, reversed의 차이가 궁금했기 때문이다.
#sorted: 정렬된 새로운 리스트 리턴(리스트에 영향 없이 새로운 리스트 리턴), sort: None리턴(리스트 자체를 정렬)
#reversed: 바뀐 새로운 리스트 리턴(리스트에 영향 없이 새로운 리스트 리턴), reverse: None리턴(리스트 자체를 역정렬)


#다른 사람의 풀이
'''
def solution(s):
    return ''.join(sorted(s, reverse=True))
'''
#아. sorted(문자열, reverse = True)를 사용하면 역정렬을 할 수 있었다! 좋은 깨달음.
