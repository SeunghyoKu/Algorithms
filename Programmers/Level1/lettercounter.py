#프로그래머스 1단계: p와 y 갯수 세기
#https://programmers.co.kr/learn/courses/30/lessons/12916

#나의 풀이: sum 이라는 변수를 만들어 거기에 저장한 후 비교함
#하지만 이렇게 return true, false할 필요가 없었던 듯 하다.
#왜냐면 이미 비교할 때 true 와 false로 결과가 나오니까.

def solution(str):
    p_sum = 0
    y_sum = 0

    for i in range(len(str)):
        if str[i] == 'p' or str[i] == 'P':
            p_sum += 1
        elif str[i] == 'y' or str[i] == 'Y':
            y_sum += 1

    if p_sum == y_sum:
        return True

    else:
        return False


#다른 사람의 풀이
#count(): 집계함수
#lower(): 소문자로 바꾸는 함수
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
