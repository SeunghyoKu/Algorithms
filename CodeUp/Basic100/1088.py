#3의 배수는 통과?
#https://codeup.kr/problem.php?id=1088

#1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되, 3의 배수인 경우는 출력하지 않도록 만들어보자.
#1부터 입력한 정수보다 작거나 같을 때까지 1씩 증가시켜 출력하되 3의 배수는 출력하지 않는다.

num = int(input())

for i in range(1, num+1):
  if i % 3 == 0:
    continue
  else:
    print(i, end = " ")
  
