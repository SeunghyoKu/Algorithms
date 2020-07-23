# 2012번: 등수매기기
# https://www.acmicpc.net/problem/2012

'''
2007년 KOI에 N명의 학생들이 참가하였다. 경시일 전날인 예비소집일에, 모든 학생들은 자신이 N명 중에서 몇 등을 할 것인지 예상 등수를 적어서 제출하도록 하였다.

KOI 담당조교로 참가한 김진영 조교는 실수로 모든 학생의 프로그램을 날려 버렸다. 1등부터 N등까지 동석차 없이 등수를 매겨야 하는 김 조교는, 어쩔 수 없이 각 사람이 제출한 예상 등수를 바탕으로 임의로 등수를 매기기로 했다.

자신의 등수를 A등으로 예상하였는데 실제 등수가 B등이 될 경우, 이 사람의 불만도는 A와 B의 차이 ( |A-B| )로 수치화할 수 있다. 당신은 N명의 사람들의 불만도의 총 합을 최소로 하면서, 학생들의 등수를 매기려고 한다.

각 사람의 예상 등수가 주어졌을 때, 김 조교를 도와 이러한 불만도의 합을 최소로 하는 프로그램을 작성하시오.
'''

# 처음 제출한 코드 - 시간 초과
def dissatisfaction(arr):
    result = 0
    for i in range(len(arr)):
        result += abs(arr[i] - (i+1))
    return result

def makingArray():
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(int(input()))
    print(dissatisfaction(sorted(arr)))

makingArray()

'''
고려하지 못한 테스트 케이스가 있을 순 있지만.. 지금의 생각으로는 잘 돌아갈 것 같은데 시간 초과가 났다.
비효율 코드 메이커 그 자체인 것 같아 조금 슬프지만 ㅠㅠ 좋은 코드를 생각해보기로 했다.

수정의 수정을 고쳐도 알 수 없어서 혹시나 PyPy3으로 돌려보았는데 정해진 시간 내에 잘 돌아갔다.
Python3으로 제출한 사람의 코드도 한 번 확인해보았다.

간단한 로직이기에 구조는 거의 동일하나 Python3으로 제한 시간을 맞춘 사람은 readlines() 함수를 대신 이용하였다.
input()보다 sys.stdin의 readline() 함수가 시간이 훨씬 짧게 걸리기 때문에 종종 사용한다고 한다.
'''


# 다른 사람의 코드
import sys
a=int(input())
b=[int(sys.stdin.readline()) for i in range(a)]
b.sort()
r=0
for i in range(a):
   r+=abs(b[i]-i-1)
print(r)
