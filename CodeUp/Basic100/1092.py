#함께 푸는 날
#https://codeup.kr/problem.php?id=1092

#같은 날 동시에 가입한 3명의 사람들이 koistudy.net을 들어와 문제를 푸는 날짜가 매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?

#예를 들어 3명이 같은날 가입/등업하고, 각각 3일 마다, 7일 마다, 9일 마다 한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게 된다.

#같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는, 방문 주기가 공백을 두고 입력된다.
#3명이 다시 모두 함께 방문에 문제를 풀어보는 날(동시 가입/등업 후 며칠 후?) 을 출력한다.

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
day = 1

while (day%a != 0) or (day%b != 0) or (day%c != 0):
  day = day +1
  
print(day)

#날짜는 1일 이후부터니까 1로 초기화해둔다.
#a, b, c 중 하나라도 나눴을 때 나머지가 있다면, day를 더한다.
#a, b, c로 모두 나누어 진다면 반복문을 끝내고 출력한다.
#최소공배수 
