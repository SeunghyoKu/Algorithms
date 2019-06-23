#입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
#(단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.)

#짜잔 세 개의 수를 비교하려면 삼항연산자 안에 삼항연산자를 넣어야 합니다.
#삼항연산자 이렇게 썼으니 안 잊어먹기를

#a i f (a<b) else b .. 혹시 모르니까 연습

a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

small = a if (a<b and a<c) else (b if (b<c and b<a) else c)
print(small)
