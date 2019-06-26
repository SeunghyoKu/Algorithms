# 바둑알 십자 뒤집기
# https://codeup.kr/problem.php?id=1097

# 바둑판(19×19)에 흰돌(1)/검정돌(0) 모두 꽉 채워놓여있을 때, n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

baduk=[[0] * 19 for i in range(19)]


# 판 입력 받기
for i in range(19):
	set = input().split()
	for j in range(19):
		baduk[i][j] = set[j]

# 십자 뒤집기 할 개수 입력 받기
n = int(input())

for i in range(n):
    # 십자뒤집기를 할 기준점
    a, b = input().split()
    a = int(a)
    b = int(b)

    #가로 열이 다 바뀌고 세로 열이 다 바껴야 되잖아
    #a-1인 이유는 바둑판을 셀 때 0부터 시작이 아니라 1부터 세니까 빼준 것
    for j in range(19):
        if baduk[a - 1][j] == '1':
            baduk[a - 1][j] = '0'
            
        else:
            baduk[a - 1][j] = '1'

        if baduk[j][b - 1] == '1':
            baduk[j][b - 1] = '0'
        else:
            baduk[j][b - 1] = 1

for i in range(19):
    for j in range(19):
        print(baduk[i][j], end=" ")
    print()
