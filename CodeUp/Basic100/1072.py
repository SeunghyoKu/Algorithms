#n개의 정수가 순서대로 입력된다. n개의 입력된 정수를 순서대로 출력해보자.

size = int(input())
num = input().split(" ")

for i in range(size):
  print(int(num[i]))
