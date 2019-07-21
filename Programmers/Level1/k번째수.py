#k번째 수
#https://programmers.co.kr/learn/courses/30/lessons/42748

#배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
#예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
#array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
#1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
#2에서 나온 배열의 3번째 숫자는 5입니다.
#배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,
#commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.


#나의 풀이
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start, end = [commands[i][0]-1][0], [commands[i][1]][0]
        arr = sorted(array[start:end])
        index = commands[i][2] -1
        answer.append(arr[index])
    return answer
    
#차근차근 푼다면 어렵지 않은 문제이지만, 중간중간 표현이 너무 복잡해질 것 같아 임시 변수에 저장후 사용하였다.
#index값에 -1을 해준 이유는 컴퓨터만 0부터 세고 사람은 1부터 세기 때문!
#사실 index값 그냥 돌렸다가 out of range 오류 보고 깨달아서 고쳤다.
#하지만 다른 사람 풀이 2를 보고 너무 복잡하게 풀었다는 것을 깨달았다!!! 이런..


#다른 사람의 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    
#단 한 줄만에 코드 구현이라니.. 파이썬 답다..
#lambda!! lambda는 익명 함수(다음 줄에 휘발성으로 사라지는!)로, 굉장히 pythonic하게 사용할 수가 있다.
#lambda에 저장한 식에 map함수를 이용해 commands를 넣어줘서 돌리는 코드.
 
 
#다른 사람의 풀이2
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
    
#접근은 나와 비슷하지만, 파이썬의 기능을 사용하여 command의 값들을 저장 후 사용하여 코드를 훨씬 간결하고 깔끔한 것 같다.
