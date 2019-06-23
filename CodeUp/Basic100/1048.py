#정수 두 개(a, b)를 입력받아 (0 <= a, b <= 10) a를 2^b 배를 출력하는 프로그램을 작성해보자.

a, b = input().split(" ")
a = int(a)
b = int(b)

print(a*(2**b))
