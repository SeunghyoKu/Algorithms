#정수가 순서대로 입력된다. 0이 아니면 입력된 정수를 출력하고 0이 입력되면 출력을 중단해보자

#배열에 저장하는 법: 그냥 배열에 저장한다.

num = input().split(" ")

for i in range(len(num)):
  if num[i] != '0':
    print(num[i])
  else:
    print(num[i])
    break
