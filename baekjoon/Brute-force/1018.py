# 백준 1018번 - 브루트포스 문제
# https://www.acmicpc.net/problem/1018

M, N = map(int, input().split(" "))


def make_board(M, N):
    board = []
    for i in range(M):
        board.append(input())
    return board


def board_checker(starter, board, index):
    answer = 0
    row, col = index
    for i in range(row, row+8):
        for j in range(col, col+8):
            # 둘 다 짝수
            if i % 2 == 0 and j % 2 == 0 and board[i][j] != starter:
                answer += 1
            # 둘 다 홀수
            elif i % 2 == 1 and j % 2 == 1 and board[i][j] != starter:
                answer += 1
            # 둘 중 하나 홀수
            elif ((i % 2 == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1)) and board[i][j] == starter:
                answer += 1
    return answer


def get_answer(board):
    answers = []
    for i in range(M - 8 + 1):
        for j in range(N - 8 + 1):
            answers.append(min(board_checker('B', board, [i, j]),
                               board_checker('W', board, [i, j])))
    return min(answers)


board = make_board(M, N)
answer = get_answer(board)
print(answer)
