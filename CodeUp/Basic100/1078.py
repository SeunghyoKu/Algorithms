#정수 한 개를 입력받아 1 부터 그 수까지 짝수의 합을 구해보자.

a = int(input())
sum = 0

for i in range(1, a+1):
  if i % 2 == 0:
    sum += i
    
print(sum)
