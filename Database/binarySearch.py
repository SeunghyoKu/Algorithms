def binary_search(array, value):
    #먼저 찾으려는 값이 있을 수 있는 상한선과 하한선을 정한다.
    #최초의 상한선은 배열의 첫 번재 값, 하한선은 마지막 값이다.

    array.sort()
    lower_bound = 0
    upper_bound = len(array) - 1

    #상한선과 하한선 사이의 가운데 값을 계속해서 확인하는 루프를 시작한다.

    while lower_bound <= upper_bound:
        midpoint = (lower_bound + upper_bound) // 2 #//: 몫

        #중간지점의 값을 확인한다.

        value_at_midpoint = array[midpoint]

        #중간 지점의 값이 찾고 있던 값이면 검색을 끝마친다.
        #그렇지 않으면 더 클지 작을지 추측한 바에 따라 상한선이나 하한선을 바꾼다.

        if value < value_at_midpoint:
            upper_bound = midpoint - 1
        elif value > value_at_midpoint:
            lower_bound = midpoint + 1
        elif value == value_at_midpoint:
            return midpoint

        #상한선과 하한선이 같아질 때까지 경계값을 줄엿다면, 찾고 있는 값이 이 배열에 없다는 것이다.
    return -1



#
arr = [1,2,5,7,9,13,15,18,33,45,77]
val = 9
print(binary_search(arr,val))
