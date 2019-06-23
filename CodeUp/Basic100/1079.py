#영문자 q 가 입력될 때까지 계속 반복하는 프로그램을 작성해보자.

str = input().split()

for i in range(len(str)):
  if str[i] != 'q':
    print(str[i])
  else:
    print(str[i])
    break
