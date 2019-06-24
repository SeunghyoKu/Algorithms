#수 나열하기1
#https://codeup.kr/problem.php?id=1089

#시작 값(a), 등차의 값(d), 몇 번째 인지를 나타내는 정수(n)가 입력될 때 n번째 수를 출력하는 프로그램을 만들어보자.

a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)

num = a + d*(n-1)
print(num)
