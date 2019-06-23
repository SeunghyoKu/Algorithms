#1부터 n까지, 1부터 m 까지 숫자가 적힌 색이 서로 다른 주사위 2개를 던졌을 때, 나올 수 있는 모든 경우를 출력해보자.

#서로 다른 주사위의 면의 개수 n, m이 공백을 두고 입력된다.

a, b = input().split()
a = int(a)
b = int(b)

for i in range(1, a+1):
  for s in range(1, b+1):
      print(i, s)
