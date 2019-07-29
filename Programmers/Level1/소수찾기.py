#소수 찾기
#https://programmers.co.kr/learn/courses/30/lessons/12921

#1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
#소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
#(1은 소수가 아닙니다.)

#시도했다 망한 코드
def solution(n):
    answer = []
    for i in range(2, n+1):
        sum = 0
        for j in range(2, n+1):
            if i % j == 0:
                sum += 1
        answer.append(sum)
            
    return len([k+2 for k in range(len(answer)) if answer[k] == 1])
#망한 코드는 잘 안 적는데 기록해본다.
#효율성따윈 개나 줘버려서 시간 초과로 통과하지 못했다. 이렇게 짜던 날이 있었다고? 싶은 날이 오길 바라며 기록용으로 남겨둔다. 또르르


#그래서 for문을 하나 더 줄여봤는데 이것도 안됐다.
def solution(n):
    answer = []
    for i in range(1, n+1):
        sum = 0
        for j in range(1, n+1):
            if i % j == 0:
                sum += 1
        if sum == 2:
            answer.append(sum)
            
    return len(answer)
    
#똑같은 문항에서 또 시간초과가 났다. 아무래도 for문 두 개 돌아가서 그런 것 같았다.

#"에라토스테네스의 체"를 이용해야 할 곳이라는 생각이 들었다.
#에라토스테네스의 체? 2보다 크거나 같고 n보다 작은 소수의 배수를 지우면서 소수를 찾는 방법
#즉, 1~n 까지의 수 중에서 소수를 뽑아낼 수 있다. => 이 문제와 찰떡 궁합인 셈

#에라토스테네스의 체를 이용한 풀이

def solution(n):
    num=set(range(2,n+1))
    for i in range(2,int((n+1)**0.5)+1):
        num -= set(range(2*i,n+1,i))
            
    return len(num)
    
#결국 모아둔 포인트(프로그래머스에서는 알맞은 코드를 제출하면 점수를 얻을 수 있다.)를 사용하여 다른 사람의 코드를 참고하여 약간의 수정을 고쳤다.
#set(): 집합 자료형으로 차집합(-), 교집합(&), 합집합(|)을 이용할 수 있어 편리하다.
#https://wikidocs.net/1015
#이 문제를 푼 사람은 차집합을 이용하여 풀었는데, 내가 수정한 부분은 에라토스테네스의 체를 이용해 좀 더 시간을 줄이기 위해 n^1/2까지 범위로 고친 후,
#n까지 모든 범위의 숫자 중에서 빼주었다.
