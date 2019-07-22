#제일 작은 수 제거하기
#https://programmers.co.kr/learn/courses/30/lessons/12935

#정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
#단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
#예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

#나의 풀이
def solution(arr):
    arr.remove(min(arr))
    if len(arr) == 0:
        arr.append(-1)
    return arr
    
    
#다른 사람의 풀이
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]
    
#최솟값 보다 큰 값들을 리스트에 담아 리턴하는 함수
#나의 풀이와 달리, 중복된 최솟값도 모두 제거해주기 때문에 더 좋은 코드라 보인다.
