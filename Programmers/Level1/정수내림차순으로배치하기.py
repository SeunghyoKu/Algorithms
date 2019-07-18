#정수 내림차순으로 배치하기
#https://programmers.co.kr/learn/courses/30/lessons/12933

#함수 solution은 정수 n을 매개변수로 입력받습니다.
#n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.


#나의 풀이
def solution(n):
    list = []
    for i in range(len(str(n))):
        list.append(str(n)[i])
    list.sort(reverse = True)

    return int("".join(list))
 
#list를 하나 만들어서, 반복문을 이용하여 n의 값을 string으로 변환 후 넣었다.
#그 후, list를 역순으로 (reverse = True)를 사용하여 정렬한 후
#"".join(list)를 사용하면 ""(띄어쓰기 없이) list의 내용들을 int형식으로 반환하였다!

#다른 사람의 풀이

def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))
    
#나처럼 list를 따로 만든 것이 아니라 바로 n을 문자열화 한 다음 list에 넣었다!
#list()함수의 사용법이 잘 기억나지 않아 나는 저렇게 푼 것이다
#오늘도 다른 사람의 코드를 보며 배웁니다.
