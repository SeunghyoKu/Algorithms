#서울에서 김서방 찾기
#https://programmers.co.kr/learn/courses/30/lessons/12919

#String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요.
#seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

#나의 풀이
#for문으로 Kim 서방을 찾아 kim 이란 변수 안에 저장하였다.
def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            kim = i
    
    return "김서방은 {}에 있다".format(kim)
    
#다른 사람의 풀이
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
    
#index함수를 사용하여서 풀었다.
#a.index(x): a에서 x의 위치를 반환하는 함수
