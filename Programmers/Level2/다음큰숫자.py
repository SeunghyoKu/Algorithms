#다음 큰 숫자
#https://programmers.co.kr/learn/courses/30/lessons/12911

#자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

#조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
#조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
#조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
#예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

#자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

#나의 풀이
def solution(n):
    numof1 = list(str(bin(n))).count("1")
    num = n + 1
    
    while list(str(bin(num))).count("1") != numof1:
        num += 1
                
    return num

#굳이 list로 만들어서 count 함수를 쓴 이유는, count함수가 list형태만을 받는 줄 알았다..
#하지만 count()는 문자열도 받아올 수 있다.
#간만의 알고리즘 문제 풀이!
