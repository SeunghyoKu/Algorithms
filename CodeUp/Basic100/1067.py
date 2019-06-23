#정수 한 개가 입력되었을 때, minus(음)/plus(양) even(짝)/odd(홀)을 출력해보자.
#첫 줄에 minus(음) 나 plus(양) 를 출력하고, 두번째 줄에 odd(홀) 나 even(짝) 을 출력한다.

num = int(input())

if num > 0:
  print("plus")
else:
  print("minus")
 
if num%2 == 0:
  print("even")
else:
  print("odd")
