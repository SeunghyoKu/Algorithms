# Level 1. 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    pang = [] # 맨 오른쪽 배열
    # 제한사항 1
    if len(board) >= 5 and len(board) <= 30 and len(board[0]) >= 5 and len(board[0]) <= 30:
        for i in range(len(moves)): # moves 요소 i 만큼 반복할 때,
            for j in range(len(board)): # board 판 만큼: 만약 없다면 다음줄로 이동...
                if board[j][moves[i]-1] != 0: # 만약 인형이 있다면!
                    pang.append(board[j][moves[i]-1]) # pang에 추가
                    board[j][moves[i]-1] = 0 # 뺀 것은 0으로 초기화
                    break
        
    return pangpang(pang,answer)

answer = 0
max_answer = []

# 터지는 함수 따로 생성 팡팡팡팡
def pangpang(arr, answer):
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]: # 만약 앞 뒤가 같다면? +2 (두 개가 터지니까)
            answer += 2
            del arr[i], arr[i-1] # 삭제해준다.
            max_answer.append(answer)
            pangpang(arr, answer) # 다시 해..
            return max(max_answer)

'''
내가 이 코드를 작성하였지만.. 이 코드는 무엇일까..?

아무튼 변수 및 함수 이름을 정하는 것이 힘들었다. 결과적으로 pangpang 함수 안에 pang 배열을 넣는 사태가 발생했다.
재귀함수로 작성해서 pangpang(pang, answer)가 반복되는 상황 ㅋㅋㅋ 웃프다.
이름을 잘 정하는 것이 중요할 것 같다.
max_answer 배열에 따로 터지는 횟수를 저장해서 그 중 max를 return 하는 방식을 사용한 까닭은..
오늘 배운 재귀함수로 구현을 했는데.. 재귀함수 특성상..
가장 처음 실행되는 함수. 첫번째 pangpang 함수를 실행했을 때의 pang 함수가 실행될 때의 answer가 자꾸 반환되는 것이었다... (2가 출력됨)
나의 의도가 아니었지만, 저장한 후 그중 max 값을 return 해주는 것으로 마무리 지었다.
'''

# 다른 사람의 코드
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
'''
stacklist의 크기가 2 이상일 때 바로 가장 뒤에 있는 것부터 확인하여 pop 해주는 코드였다.
간결하고 가독성이 좋아서 참고하려 가져와보았다.
이 외에도 다른 풀이들이 많아서 참고하면 좋을 거 같았지만.. 직접 가서 참고하도록 하자.
'''
