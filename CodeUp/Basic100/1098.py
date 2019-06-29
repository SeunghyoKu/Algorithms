# 설탕과자 뽑기
# https://codeup.kr/problem.php?id=1098

# 격자판에 막대기를 놓는 모든 방법을 살펴본 후 가장 큰 설탕과자를 얻을 수 있는 방법을 알아내기 위해

# 격자판에 막대기를 놓는 기본적인 상황을 바둑판에 바둑알 놓기처럼 만들어보고자 하였다.

# 격자판의 세로(h), 가로(w), 막대의 개수(n)와 각 막대의 길이(l), 막대를 놓는 방향(d: 가로는 0, 세로는 1)과
# 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때, 격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

# 입력
# 첫 줄에 격자판의 세로(h), 가로(w)가 공백을 두고 입력되고,
# 두 번째 줄에 놓을 수 있는 막대의 개수(n), 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.

# 출력
# 모든 막대를 놓은 격자판의 상태를 출력한다. 막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.

h, w = input().split()
# 세로와 가로 입력받기
h = int(h)
w = int(w)

# 막대의 수
n = int(input())
makdae = [[0] * 100 for i in range(100)]  # 막대를 저장할 리스트

for i in range(n):
    l, d, x, y = input().split()
    l = int(l)
    d = int(d)
    x = int(x)
    y = int(y)

    xx = x - 1
    yy = y - 1

    #가로일 때
    if d == 1:
        for length in range(l):
            makdae[xx][yy] = 1
            xx += 1

    #세로일 때
    else:
        for length in range(l):
            makdae[xx][yy] = 1
            yy += 1

#높이를 먼저 받고 그 다음에 #너비를 반복해
for i in range(h):
    for j in range(w):
        print(makdae[i][j], end=" ")
    print()
