#2016년의 날짜를 입력 받아 요일을 리턴하는 함수를 만들기!
#a, b = a월 b일
#2월이 윤달입니다

def solution(a, b):
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [1,2,3,4,5,6,7,8,9,10,11,12]
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    #만약에, 3월이면, 1-3월 날짜 다 합친거를 7로 나눈 것의 나머지 = 요일
    sum = 0

    if a > 1:
        for i in range(a-1):
            #days[a-1] 전까지의 sum을 구하자
            sum = days[i]+sum
        sum = sum + b
    elif a == 1:
        sum = b

    #날짜는 1일부터 시작하니까 마지막에 -1 하도록 하자
    findday = sum%7 - 1

    answer = day[findday]
    return answer
