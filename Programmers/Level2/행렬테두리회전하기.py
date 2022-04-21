def solution(rows, columns, queries):
    array = [[0 for col in range(columns)] for row in range(rows)]
    answer = []
    
    for row in range(rows):
        for col in range(columns):
            array[row][col] = (row) * columns + col + 1
    
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1 # 칸 에 있는 값과 index가 다르다.
        temp = array[x1][y1]
        least = temp
        
        # 좌측 상향
        for k in range(x1, x2):
            tmp = array[k + 1][y1]
            array[k][y1] = tmp
            least = min(least, tmp)
        # 하측 좌향
        for k in range(y1, y2):
            tmp = array[x2][k + 1]
            array[x2][k] = tmp
            least = min(least, tmp)
        # 우측 하향
        for k in range(x2, x1, -1):
            tmp = array[k - 1][y2]
            array[k][y2] = tmp
            least = min(least, tmp)
        # 상측 우향
        for k in range(y2, y1, -1):
            tmp = array[x1][k - 1]
            array[x1][k] = tmp
            least = min(least, tmp)

        # 과정속에서 사라져버린 기존 첫번째 칸을 대입해준다.
        array[x1][y1 + 1] = temp
        answer.append(least)
        
    return answer
