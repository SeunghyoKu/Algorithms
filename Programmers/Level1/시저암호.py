#시저 암호
#https://programmers.co.kr/learn/courses/30/lessons/12926

#어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
#예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다. z는 1만큼 밀면 a가 됩니다.
#문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

#나의 풀이
def solution(s, n):
    #lower에 소문자 알파벳, upper에 대문자 알파벳을 저장
    #아까 배운 map()함수에 lambda를 사용해봤습니다.
    lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper = list(map(lambda i: i.upper(), lower))
    
    #값을 저장할 arr 리스트 선언
    arr = []
    
    for i in range(len(s)):
        #공백은 공백대로 유지해야 하기 때문에, 서로 다른 케이스로 다뤄줍니다.
        if s[i] != " ":
            #만약 소문자일 경우
            if s[i].islower():
                sum = lower.index(s[i]) + n
                #while문을 이용해서 26보다 클 경우(알파벳의 총 갯수가 26임) 26을 빼주는 반복문 실행
                while sum > 25:
                    sum -= 26
                else:
                    arr.append(lower[sum])
            
            #만약 대문자일 경우
            else:
                sum = upper.index(s[i]) + n
                while sum > 25:
                    sum -= 26
                else:
                    arr.append(upper[sum])
        #공백일 경우 공백을 추가해준다.        
        elif s[i] == " ":
            arr.append(" ")
   #리스트의 형태로 받았기 때문에, 반환하는 값은 join 함수를 이용하여 출력해줍니다.
   return "".join(arr)
    
#억. 이 문제 레벨1인데도 풀이가 무지 길다!!
#그래서 코드에 주석을 달아보았습니다.
#아쉬운 건.. 26을 빼지 않고 26을 나눈 나머지였다면 더 좋았을 것 같다. 꼭. 풀고 나면 생각이 나지..


#다른 사람의 풀이
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
 
#ord(): 아스키 값을 돌려주는 함수 
#chr(): 아스키 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수
#다른 사람들의 풀이를 볼 때마다. 공부를 더 열심히해야겠구나 하는 생각이 듭니다.. :0.
#코드업 기초 100제를 풀 때 봤던 아스키 코드를 이용한 풀이법이다.
