#자릿수 더하기
#https://programmers.co.kr/learn/courses/30/lessons/12931

#자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
#예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

#나의 풀이
def solution(n):
    num = str(n)
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    return sum
#이번 문제는 다른 사람들의 풀이가 좋고, 나의 코드 난이도가 높지 않아 달 주석이 없다!
    
    
#다른 사람의 풀이1
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10)
#재귀 함수를 이용한 풀이! 엄청나..


#다른 사람의 풀이2
def sum_digit(number):
    return sum([int(i) for i in str(number)])
#3항연산자로 풀이! 전체적인 접근은 나의 풀이와 같으나 삼항연산자를 이용하여 더 깔금해 보인다.
#왜 3항연산자는 익숙해지지 않을까


#다른 사람의 풀이3
def sum_digit(number):
    '''number의 각 자릿수를 더해서 return하세요'''
    return sum(map(int,str(number)))
#map() 함수 이용! map을 이용한 간단한 풀이들이 많은 것 같다.
#map()을 이용하여 뜯어서 리스트에 저장한 후, 다시 sum을 하여 리스트의 요소들을 더하는 풀이.
