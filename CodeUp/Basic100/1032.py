#10진수를 입력받아 16진수(hexadecimal)로 출력하는 프로그램을 작성해보자.

#1031번에 더 자세한 풀이를 적어두었습니다.

num = int(input())
hexa = hex(num)[2:]

print(hexa)
