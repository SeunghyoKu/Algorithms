#입력된 두 정수 a, b 중 큰 값을 출력하는 프로그램을 작성해보자.
#(단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.)

#삼항 연산자: 항이 3개인 형태일 때


a, b = input().split(" ")
a = int(a)
b = int(b)

c  = a if a>b else b
print(c)

#파이썬의 3항 연산자
#(조건을 충족할 때) if (맞는 조건) else (조건을 충족하지 않을 때)
#ex: a if a>b else b
