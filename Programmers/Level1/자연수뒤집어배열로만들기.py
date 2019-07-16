#자연수 뒤집어 배열로 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12932

#자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

#나의 풀이
def solution(n):
    answer = []
    for i in range(len(str(n))):
        answer.append(int(str(n)[i]))
        
    return list(reversed(answer))
    
    
#음.. 총체적 난국.. 이 스파게티 코드는 뭘까? 아무튼 돌아가긴 한다.
#len()에 정수형이 안들어가길래 str으로 바꾼 후 넣었고
#append도 비슷한 연유로 str을 int로 바꾼 다음에 또 int로 바꾸는 짓을 함..
#reversed(answer)은 리스트로 반환하지 않기 때문에 다시 list에 넣어주었다.


#다른 사람의 풀이
def digit_reverse(n):
    return list(map(int, reversed(str(n))))

#map(f, iterable)함수는?
#map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.
#map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.

#map()을 이용하여 int형식으로 바꾸고, reversed된 string화 된 n을 반복적으로 list형식으로 입력 받는 것 <- 한국말이 더 어렵다..

#다른 사람의 풀이2
def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]
    
#리스트에서 거꾸로 출력하기! [::-1] <- -1을 세번째에 넣어주면 거꾸로 나온다.
#3항연산자를 활용했다.. 
