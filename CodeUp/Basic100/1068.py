#점수(정수)를 입력받아 평가를 출력해보자.

a = int(input())

if a>=90 and a<=100:
  print("A")
elif a<90 and a>=70:
  print("B")
elif a<70 and a>=40:
  print("C")
else:
  print("D")
