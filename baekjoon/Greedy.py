# 5585 - 거스름돈
# https://www.acmicpc.net/problem/5585

'''
타로는 자주 JOI잡화점에서 물건을 산다. JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 언제나 거스름돈 개수가 가장 적게 잔돈을 준다. 타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.

예를 들어 입력된 예1의 경우에는 아래 그림에서 처럼 4개를 출력해야 한다.
'''

coin_list = [500,100,50,10,5,1]
changes = 1000 - int(input())
answer = 0

for coin in coin_list:
    answer += changes // coin
    changes %= coin

print(answer)

# 그리디를 활용한 대표적인 문제이다.
# 무조건 큰 단위부터 먼저 돌려주기 때문에 단위가 담긴 coin_list는 큰 단위로 작성한다.
