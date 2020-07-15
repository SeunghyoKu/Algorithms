# https://programmers.co.kr/learn/courses/30/lessons/42584
# 주식가격
# Stack & Queue 이용 문제

def solution(prices):
    pricesLength = len(prices)
    answer = [0 for i in range(pricesLength)]
    
    for i in range(pricesLength):
        for j in range(i+1, pricesLength):
            answer[i] += 1
            if prices[i] > prices[j]:
                break
                
    return answer

# prices의 length를 사용하는 부분이 많아 따로 변수에 저장해 반복적으로 사용하였다.
# 편의를 위해 answer 리스트에 0을 넣어둔 값으로 초기화를 해두었다.
# 첫번째 for문 안에서 [i:] 만큼 반복하면서 지나가게 되는데,
# 첫 풀이 때에는 prices[i] <= prices[j] 일때만 answer의 각 요소에 +1을 해주었으나
# 마지막 값이 아닐 때 빼고는 바로 시간이 줄어들지라도 바꾸기 직전까지 1초로 취급하므로
# 조건문에 들어가기전 +1을 해주었고, prices[i]가 더 크다면 break문을 사용해 반복문을 빠져 나와 효율성을 높여주었다.
