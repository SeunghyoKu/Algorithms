# 문제 링크: https://www.acmicpc.net/problem/9093

배열과 문자열 처리에 대한 간단한 이해를 할 수 있는 문제!

# 내 코드
num = int(input())

for i in range(num):
    list =  []
    cmd = input().split() # 띄어쓰기 부분 띄워 저장함
    for j in range(len(cmd)):
        list.append(cmd[j][::-1])
    print(" ".join(list))
