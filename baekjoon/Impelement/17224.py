# 백준 17224번 문제 - APC는 왜 서브태스크 대회가 되었을까?
# https://www.acmicpc.net/problem/17224

'''
첫 줄에 문제의 개수 N, 현정이의 역량 L, 현정이가 대회중에 풀 수 있는 문제의 최대 개수 K가 주어진다.
둘째 줄부터 N개의 줄에 걸쳐 1 ~ N번째 문제의 쉬운 버전의 난이도 sub1, 어려운 버전의 난이도 sub2 가 순서대로 주어진다.

현정이가 APC에 참가했다면 얻었을 점수의 최대값을 출력한다.
'''

N, L, K = list(map(int, input().split()))
easy, hard = 0, 0

for i in range(N):
    sub1, sub2 = list(map(int, input().split()))
    
    # sub1, sub2가 모두 풀 수 있는 난이도일 때
    if sub1 <= L and sub2 <= L:
        hard += 1
    # sub1은 풀 수 있으나, sub2는 풀 수 없는 난이도일 때
    elif sub1 <= L and sub2 > L:
        easy += 1

# hard 문제의 경우
# 총 풀 수 있는 양 K와 풀 수 있는 hard한 문제 중 작은 만큼 풀 수 있다.
ans = min(K, hard) * 140

# easy 문제의 경우
# 이게 추가 점수 받을 수 있는 부분
# K - hard (하드한 거 못풀고 남은 문제), easy한 문제 중에서 더 작은 것만큼 풀 수 있다.
if hard < K:
    ans += min(K - hard, easy) * 100
    
print(ans)
