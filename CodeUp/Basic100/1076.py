#영문자 한 개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자. (a ~ z)

#range 사용법 range(a, b+1) : a부터 b까지 반복
#ord(아스키 코드로 바꾸기)
#chr(다시 원래 문자열로 바꾸기)
#a 가 97이라서 97부터 계산하였다.

letter = ord(input())

for i in range(97, letter+1):
  print(chr(i), end = " ")
