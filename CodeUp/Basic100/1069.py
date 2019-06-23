#평가(A, B, C, D, ...)를 문자로 입력 받아 내용을 다르게 출력해보자.
'''
평가내용
평가 : 내용
D : slowly~
C : run!
B : good!!
A : best!!!
나머지문자들 : what?
'''

#헉.. 파이썬엔 switch 가 없다.
#대신 쩌는 elif 가 있다.

a = input()

if a == "A":
  print("best!!!")
elif a == "B":
  print("good!!")
elif a == "C":
  print("run!")
elif a == "D":
  print("slowly~")
else:
  print("what?")
