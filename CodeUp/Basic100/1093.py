#이상한 출석 번호 부르기1
#https://codeup.kr/problem.php?id=1093

#출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.
#첫 번째 줄에 출석 번호를 부른 횟수 정수 n이 입력된다.

n = int(input())
call = input().split()

students = [0]*23

for i in range(len(call)):
  students[int(call[i])-1] += 1 
  
for i in range(len(students)):
  print(students[i], end = " ")

#오류가 엄청 났었는데, 그 이유는 call 에 저장한 input 값들이 str값이기 때문이었다.
#그래서 int로 감싼 후 정수로 바꿔 계산하였다.
