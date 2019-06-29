#나누어 떨어지는 숫자 배열
#https://programmers.co.kr/learn/courses/30/lessons/12910

#array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
#divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

#나의 풀이
def solution(arr, divisor):
    #answer라는 배열을 만들어 저장
    answer = []

    #arr의 길이 만큼 반복하자!
    for i in range(len(arr)):
        #만약 나머지가 0이라면 answer에 저장하자
        if arr[i] % divisor == 0:
            answer.append(arr[i])

    #만약 저장된 게 없다면 -1을 저장하자
    if len(answer) == 0:
        answer.append(-1)

    #sort()는 자동으로 오름차순으로 정렬해준다.
    else:
        answer.sort()

    return answer
