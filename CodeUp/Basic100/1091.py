#수 나열하기
#https://codeup.kr/problem.php?id=1091
#예를 들어 1 -1 3 -5 11 -21 43 ... 은 1부터 시작해 이전에 만든 수에 -2를 곱한 다음 1을 더해 다음 수를 만든 수열이다.
#시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)가 입력될 때, n번째 수를 출력하는 프로그램을 만들어보자.

a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)
num = a

for i in range(n-1):
  num = num * m +d
print(num)
