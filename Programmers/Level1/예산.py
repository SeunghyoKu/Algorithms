#예산
#https://programmers.co.kr/learn/courses/30/lessons/12982

"""
S사에서는 각 부서에 필요한 물품을 지원해 주기 위해 부서별로 물품을 구매하는데 필요한 금액을 조사했습니다.
그러나, 전체 예산이 정해져 있기 때문에 모든 부서의 물품을 구매해 줄 수는 없습니다. 그래서 최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 합니다.

물품을 구매해 줄 때는 각 부서가 신청한 금액만큼을 모두 지원해 줘야 합니다. 예를 들어 1,000원을 신청한 부서에는 정확히 1,000원을 지원해야 하며,
1,000원보다 적은 금액을 지원해 줄 수는 없습니다.

부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때,
최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수를 완성해주세요.
"""

#나의 코드
def solution(d, budget):
    d.sort()
    sum = 0
    answer = 0
    
    for i in range(len(d)):
        #sum에 d[i]을 차례로 더해주고
        sum += d[i]
        
        #그 값이 크거나 작으면 answer 개수 +1
        if sum <= budget:
            answer += 1
        #아니면 break 로 반복문을 끝내버린다.
        else:
            break
    return answer
    
#sort()를 사용한 이유: 순서대로 정렬한 후 차례로 더하는 것이 더 많은 부서를 지원하는 데 도움이 될 거라 생각했다.
#answer는 리턴할 값, sum은 budget보다 크거나 작은지 비교하기 위한 값

#다른 사람 풀이

def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
    
#pop(): pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다.
#sort 후에 pop을 하면 가장 큰 수가 사라지겠지?
#그 수를 pop한 후 budget 과 같거나 작은 수가 된다면, d의 길이를 돌려주면 되는 것이다
#효율이 훨씬 좋은 풀이!
