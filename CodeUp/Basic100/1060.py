#입력 된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.

#비트 연산자 and = &하나 쓰기
#그럼 비트연산자 and 가 뭔데? : 둘 다 값이 1일 경우 1을 반환!
a, b = input().split(" ")
a = int(a)
b = int(b)

print(a&b)
