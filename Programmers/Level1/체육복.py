# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862
# 그리디 알고리즘

#점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.
#학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
#예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다.
#체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

#전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
#체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

#제한 사항

#전체 학생의 수는 2명 이상 30명 이하입니다.
#체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
#여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
#여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
#여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며,
#남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.



#굉장히 오랜만에 푸는 문제다.. 그동안 아프고 바쁜 일이 많았어서.. 다시 꾸준히 풀도록 노력해야겠다.

#나의 풀이
def solution(n, lost, reserve):

    #예외 중 잃어버린 학생 중 여벌을 가져온 경우, 본인이 그 체육복을 입기 때문에, 이 경우의 학생들을 제외한 새로운 lost, reserve 리스트를 만든다.
    after_lost = [l for l in lost if l not in reserve]
    after_reserve = [r for r in reserve if r not in lost]
    
    #그리디 알고리즘을 이용하여, 일단 왼쪽의 학생을 우선적으로 체육복을 빌려주는 것으로 생각했다.
    for i in after_reserve:
        if i - 1 in after_lost:
            after_lost.remove(i - 1)
            
        #왼쪽이 없으면 오른쪽에서 빌려야지!
        elif i + 1 in after_lost:
            after_lost.remove(i + 1)
            
    return n - len(after_lost)
    
    
'''
그리디 알고리즘을 이용한 문제입니다.
그리디 알고리즘에 대해 학습해봤습니다.

- 그리디(Greedy) 알고리즘?
  이름대로 탐욕적입니다.
  미래 생각 없이! 현 시점에서 최선의 선택을 하는 기법입니다.
  무조건 크게, 작게, 길게, 짧게하는 등 극단적으로 방법이 제공된다.
  
  모든 경우에서 해결책이 되지 않기 때문에, 다이나믹 프로그래밍 등과 함께 사용되는 등 보완이 필요한 경우도 있다.

'''

#다른 사람의 풀이
def solution(n, lost, reserve):
    answer = 0
    
    student = []
    
    for i in range(n):
        student.append(0)
        
    for i in lost:
        student[i-1] -= 1
    
    for i in reserve:
        student[i-1] += 1

    for i in range(0, len(student)):
        if student[i] == 1:
            if i -1 >= 0:
                if student[i-1] == -1:
                    student[i-1] += 1
                    student[i] -= 1
        
        if student[i] == 1:           
            if i + 1 < len(student):
                if student[i+1] == -1:
                    student[i+1] += 1
                    student[i] -= 1
                
    for stu in student:
        if stu >= 0:
            answer += 1
    return answer
 
 #잃어버린 학생만큼 체육복을 -1, 여벌을 가져온 학생만큼 +1 하여 구하는 방법
 #직관적이라 좋은 방법 같다.
