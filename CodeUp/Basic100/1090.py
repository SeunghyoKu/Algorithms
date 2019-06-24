#등비 수열
#https://codeup.kr/problem.php?id=1090

#시작 값(a), 등비의 값(r), 몇 번째 인지를 나타내는 정수(n)가 입력될 때 n번째 수를 출력하는 프로그램을 만들어보자.

a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)

num = a * (r **(n-1))
print(num)
