#문자열 다루기
#https://programmers.co.kr/learn/courses/30/lessons/12918

#문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
#예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

#나의 풀이
#isnumeric(): 숫자값 표현하는 문자까지 포함해서 숫자인지 아닌지 판별해준다
#아쉬운 점은.. return 할 값에다가 if문 안에 들어가는 조건문을 썼어도 똑같은 값이었을 거라는 것

def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isnumeric() == True:
        return True
    else:
        return False
        
#다른 사람의 풀이
#isdigit(): 문자열에 사용된 글자들이 digit인지 아닌지 판별해준다 (한마디로 숫자로 된 문자열인지?)
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)



