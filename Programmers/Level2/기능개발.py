# 기능개발 - 스택 & 큐 문제
# https://programmers.co.kr/learn/courses/30/lessons/42586

# 나의 풀이
def solution(progresses, speeds):
    answer = []
    while len(progresses) > 1:
        num = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        while progresses[0] >= 100 and len(progresses) > 1:
            num += 1
            progresses.pop(0)
            speeds.pop(0) 
        if num != 0:
            answer.append(num)
            
    # 이유는 모르겠으나 마지막 부분에서 자꾸 뻑이 나서 이처럼 마지막 항은 따로 처리해주었음 :-(
    if len(progresses) == 1:
        if progresses[0] >= 100:
            answer[-1] += 1
        else:
            answer.append(1)
            
    return answer

'''
speeds도 pop 해줘야 되는데 깜빡해서 생각보다 오래 걸렸던 문제임
꼼꼼하게 문제를 살펴 보게씁니다.
'''


# 다른 사람의 풀이 1
def solution(progresses, speeds):
    answer = []
    while progresses:
        num = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        while progresses:
        # 위에서는 while progresses[0]으로 반복문을 돌리려다보니 오류가 났다.
        # 없더라도 돌아갈 수 있어야 되기 때문에 이 분의 풀이처럼 먼저 while progresses 하고, if문을 아래에 적으면 좋은 것 같다.
            if progresses[0] >= 100:
                num += 1
                progresses.pop(0)
                speeds.pop(0)
            else:
                break
        if num != 0:
            answer.append(num)   
              
    return answer

# 다른 사람의 풀이 2
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
    # -((p-100)//s 로 하면 ceil((100-p)//s)를 하지 않아도 된다.
    # 만약에, 예상 일수가 더 늦다면.. (더 크다면) 큐에 추가
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        # 만약에 기조의 예상 일수랑 같거나 작다면 기존 일수에 +1 해주는 원리
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

'''
파이썬의 zip()을 이용하면 동일한 길이의 리스트끼리 하나로 묶을 수 있다.
'''
