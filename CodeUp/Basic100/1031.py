#10진수를 입력받아 8진수로 출력하는 프로그램을 작성해보자.


#파이썬에는 진수를 변환하는 내장 함수가 존재한다!
#oct(num): 8진법, bin(num): 2진법, hex(num): 16진법

num = int(input())
oct = oct(num)
print(oct[2:])
#파이썬에서 oct함수로 변경 하면 앞에 8진수라는 의미로 o0이 함께 출력되기 때문에 답 제출을 위해서 앞의 두 글자를 잘라주었다.
