#정수 두 개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력하는 프로그램을 작성해보자.
#정수 두 개(a, b)가 공백을 두고 입력된다.

a, b = input().split(" ")
c = int(a)%int(b)
print(c)
