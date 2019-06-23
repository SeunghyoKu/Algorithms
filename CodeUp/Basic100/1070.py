#월이 입력될 때 계절이 출력되도록 해보자

mon = int(input())

if mon == 12 or mon ==1 or mon ==2:
  print("winter")
elif mon == 3 or mon == 4 or mon == 5:
  print("spring")
elif mon == 6 or mon == 7 or mon == 8:
  print("summer")
else:
  print("fall")
