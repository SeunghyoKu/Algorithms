# https://programmers.co.kr/learn/courses/30/lessons/12899

# 124 나라의 숫자

# 124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.
# 124 나라에는 자연수만 존재합니다.
# 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.

# n	result
# 1	1
# 2	2
# 3	4
# 4	11

# 나의 코드
def solution(n):
  answer = ''
  if n <= 3:
    answer = '124'[n-1]
  else:
    quotient, remainder = divmod(n, 3)
    answer = solution(q) + '124'[remainder]
  return answer
  
# 처음에는 3진수로 문제를 풀려했으나 생각보다 0을 4로 바꾸는 과정이 까다롭고 길어 배열과
# 재귀 함수를 이용하게 되었다.

# divmod 는 몫과 나머지를 튜플 형태로 리턴하는 함수
