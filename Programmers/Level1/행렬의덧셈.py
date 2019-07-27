#행렬의 덧셈
#https://programmers.co.kr/learn/courses/30/lessons/12950

#나의 풀이
def solution(arr1, arr2):
    #그냥 초기화 할 때 arr1이나 arr2의 사이즈와 같기 때문에 준 후 나중에 바꾸었다.
    answer = arr1
    
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
                
    return answer
    
#다른 사람의 풀이
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer
    
#zip(): 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
#예: zip([1,2,3], [4,5,6]) = (1,2), (3,4), (5,6)
#https://wikidocs.net/32#zip

