# 이상한 출석 번호 부르기3
#https://codeup.kr/problem.php?id=1095

#출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

#번호를 부른 횟수(n)가 첫 줄에 입력된다. (n, 1 ~ 10000)
#부른 횟수 만큼 랜덤 번호(k)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다. (k, 1~23)

n = int(input())
k = input().split()
num = []

for i in range(len(k)):
    num.append(int(k[i]))

print(min(num))

#왜 num이란 리스트를 새로 만들어 저장했을까?
#1094와 같은 이유로 우리가 입력받아 저장한 리스트 k의 값들은 string이기 때문이다.
#우리는 값의 크기를 비교하기 위해 int로 된 값이 필요하여 리스트를 새로 만들었다.

#list.append(value) : list 에 value 값을 마지막 항에 추가
#min(list): list중에서 최솟값 항 찾기
