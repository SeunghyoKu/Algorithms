#이상한 문자 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12930

#문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
#각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

#나의 풀이
def solution(s):
    #공백으로 나눠 리스트에 저장해주었다.
    list = s.split(" ")
    answer = []
    
    #리스트의 크기(단어 갯수만큼 반복해라)
    for i in range(len(list)):
        #리스트 요소의 길이(단어 하나하나의 길이만큼 반복해라)
        for j in range(len(list[i])):
        
            #만약 짝수번째라면 대문자
            if j%2 == 0:
                answer.append(list[i][j].upper())
            #만약 홀수번째라면 소문자
            else:
                answer.append(list[i][j].lower())
        #단어가 끝나면 띄어쓰기를 해준다.
        answer.append(" ")
    #근데 띄어쓰기를 해주면 마지막이 " " 공백으로 남기 때문에, 마지막 것을 지워주었다.
    del answer[len(answer) -1]
    
    #join을 이용해 answer 리스트를 문자열로 출력해준다.
    return "".join(answer)
    
#내가 봤을 때 이 문제의 제목은 이상한 문자 만들기 이지만, 결국 나에게는 이상한 코드 만들기가 되어버린듯.
#마지막 join에서 answer[:-1]로 했다면 del 함수를 쓰지 않아도 됐을 것 같다.


#다른 사람의 풀이
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

#이 긴 코드가 이렇게 된다고...? 이것이 파이썬입니까 는 드립이고 아무튼 lambda를 쓰면 정말 짧게 코드를 쓸수 있구나 싶다.
#enumerate 를 이렇게 써야 하는구나.
