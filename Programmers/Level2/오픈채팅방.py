def solution(record):
    answer = []
    users = {}
    
    for i in range(len(record)):
        recordlist = record[i].split(" ")
        lists = [recordlist[1], '님이 ','']
        if recordlist[0] == "Enter":
            lists[2] = "들어왔습니다."
            users[recordlist[1]] = recordlist[2]
            answer.append(lists)
        elif recordlist[0] == "Leave":
            lists[2] = "나갔습니다."
            answer.append(lists)
        elif recordlist[0] == "Change":
            users[recordlist[1]] = recordlist[2]
        
    for i in range(len(answer)):
        answer[i][0] = users[answer[i][0]]
        answer[i] = ''.join(answer[i])
        
    return answer
