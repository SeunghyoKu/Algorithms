#정수가 순서대로 입력된다. 0이 아니면 입력된 정수를 출력하고 0이 입력되면 출력을 중단해보자.

#이전에 있던 문제랑 무엇이 다른지요..?
#아무튼 다시 풀었습니다.

a = input().split()

for i in range(len(a)):
  if a[i] != '0':
    print(a[i])
  else:
    print(a[i])
    break
