#모의고사
#https://programmers.co.kr/learn/courses/30/lessons/42840

#수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
#수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

#1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
#2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
#3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

#1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
#가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

def solution(answers):
    score = [0,0,0]
    sheet1 = [1,2,3,4,5]
    sheet2 = [2,1,2,3,2,4,2,5]
    sheet3 = [3,3,1,1,2,2,4,4,5,5]
    
    for idx, answer in enumerate(answers):
        if answer == sheet1[idx % len(sheet1)]:
            score[0] += 1
        if answer == sheet2[idx % len(sheet2)]:
            score[1] += 1
        if answer == sheet3[idx % len(sheet3)]:
            score[2] += 1
    result = []
    for i in range(3):
        if score[i] == max(score):
            result.append(i+1)
    
    return result
    
#완전 탐색? Brute Force?: 모든 경우의 수를 하나하나 탐색하여 답을 찾는 방법을 의미한다.
# => 가능 방법을 전부 파악하는 알고리즘
# => 틀릴 일은 없으나, 탐색 시간은 오래 걸림

#idx를 sheet(각 학생의 답지 길이)변수의 길이로 나눈 나머지 값을 인덱스 값으로 사용했다!
#처음엔, 각각 답안지 값들을 반복 시켜서 돌리는 걸 생각했는데 효율성이 똥이라서, 적게 사용하는 방법을 생각했다.

#다른 사람의 풀이2

 
#itertools 모듈의 cycle을 사용하였다.
#내가 처음에 생각했던 모든 답안을 불러오는 방법인데, 나는 이런 갓갓 모듈의 존재를 몰랐다.
#cycle: 리스트 내 자료를 무한 반복 하는 경우 사용한다. (요일 같은 걸 출력할 때도 사용된다)
#https://itholic.github.io/kata-supo/
#이 분의 블로그에서 본 코드이다!
