def bubble_sort(list):
    unsorted_until_index = len(list) -1
    sorted = False

    #배열이 완전히 정렬됐음을 알 때까지 루프를 발생시킨다.
    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            #교체를 하게 되면 false로 바꿔준다.
            #이렇게 하면, 정렬이 끝나면 정렬이 되어 끝이 나게 된다.
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
        #기존에 가리키고 있던 인덱스가 정렬된 상태이므로 값 -1해준다.
        unsorted_until_index = unsorted_until_index -1


#사용예시
list = [65,55,45,35,25,15,10]
bubble_sort(list)
print(list)
