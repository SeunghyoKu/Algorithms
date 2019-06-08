#가운데 글자를 반환하는 함수 만들기 !


def solution(s):
    #글자의 수가 짝수일 때는 가운데 두 글자를 반환
    #글자의 수를 알기 위해 len()함수를 사용
    #파이썬에서 문자열의 위치의 문자를 알고 싶을땐 문자열[숫자] 와 같이 쓴다
    
    if len(s)%2 == 0:
        answer = s[len(s)//2-1]+s[len(s)//2]
    
    #글자의 수가 짝수일 때는 가운데 한 글자를 반환
    else:
        answer = s[len(s)//2]
        
    return answer
