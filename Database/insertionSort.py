def insertion_sort(array):
    #하나의 배열을 순회하는 루프
    for index in range(1, len(array)):
        #현재의 인덱스를 index에 저장한다.
        position = index
        tempo_value = array[index]

        #position 왼쪽의 값이 temp_value 보다 클 때
        #왼쪽 값을 한 셀 오른쪽으로 옮긴 후 position 값을 1 감소시킨다.
        #새 position의 왼쪽 값이 temp_value보다 큰지 확인
        #이 과정을 새 position의 왼쪽 값이 temp_value가 작을 때까지 반복
        while position > 0 and array[position - 1] > tempo_value:
            array[position] = array[position - 1]
            position = position -1

        #temp_value를 배열의 공백에 삽입한다.
        array[position] = tempo_value
