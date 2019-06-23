#정수 두 개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈값을 자동으로 계산해보자.
#정수 두 개(a, b)가 공백을 두고 입력된다.
'''
출력 기준
첫 줄에 합
둘째 줄에 차(a-b)
셋째 줄에 곱,
넷째 줄에 a를 b로 나눈 몫,
다섯째 줄에 a를 b로 나눈 나머지,
여섯째 줄에 a를 b로 나눈값(실수, 소수점 셋째 자리에서 반올림해 둘째 자리까지 출력)
을 출력한다.
'''

a, b  = input().split(" ")
a = int(a)
b = int(b)

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print('%.2f' %(a/b))

#처음에 마지막 문장을 print(round(a/b,2))로 작성했는데 작동되지 않았다.
#어떤 경우에는.. 둘째짜리 까지 출력이 안되기 때문이었다.
#'%.2f' <- 로 형식을 정해두고 값에 넣.기 소숫점 둘째 자리까지니까 .2f 인 것이다.