# 백준 17269번 - 이름궁합문제
# 문자열 처리 문제

# https://www.acmicpc.net/problem/17269

'''
입력-
첫 번째 줄에 이름의 길이 N과 M을 받는다. (2 ≤ N, M ≤ 100)
다음 줄에 이름 A와 B를 입력받는다. 이름은 반드시 알파벳 대문자만 주어진다.
출력- A와 B의 이름궁합이 좋을 확률을 %로 출력한다. 단, 십의 자리가 0일 경우엔 일의 자리만 출력한다.
'''
# 굉장히 오랜만에 푼 문제라 코드가 길고 난잡하다.. ㄸ..ㅠㅠ

# 딕셔너리를 이용해 알파벳과 획수를 함께 저장하였다.
alphabet = {"A":3, "B":2, "C":1, "D":2, "E":4, "F":3, "G":1, "H":3, "I":1, "J":1,
            "K":3, "L":1, "M":3, "N":2, "O":1, "P":2, "Q":2, "R":2, "S":1, "T":2,
           "U":1, "V":1, "W":1, "X":2, "Y":2, "Z":1}

# 입력값을 받아주었다.
a_length, b_length = input().split()
a_length, b_length = int(a_length), int(b_length)
a,b = input().split()

# name 변수에 합친 이름을 저장하였다.
# 남은 이름은 뒤에 붙여준다.

name = ''
if a_length == b_length:
    for i in range(a_length):
        name = name + a[i] + b[i]

elif a_length > b_length:
    for i in range(b_length):
        name = name + a[i] + b[i]
    name = name + a[b_length:]
    
else:
    for i in range(a_length):
        name = name + a[i] + b[i]
    name = name + b[a_length:]

# 해당 변수를 자주 사용할 것같아 따로 저장해주었다.
name_length = a_length + b_length
match_point = []

# 알파벳을 획수로 바꿔준다.
for j in range(name_length):
    match_point.append(alphabet[name[j]])

# 이제 이름 궁합을 보는 과정
# 2글자 남을때까지 하므로, 이름 전체 길이 -2 만큼 반복해준다.
for matching in range(name_length - 2):
    # 각 줄마다 마지막 항은 삭제하므로 전체 이름 길이 -1 만큼 반복한다.
    for k in range(name_length - 1):
        if match_point[k] + match_point[k + 1] < 10:
            match_point[k] = match_point[k] + match_point[k + 1]
        # 10보다 클 경우, -10하여 일의 자리만 반영한다.
        else:
            match_point[k] = match_point[k] + match_point[k + 1] - 10
    # 전체 이름의 길이가 1만큼 줄어들었으므로 -1하여 새로 저장한다.
    name_length = name_length - 1
    # 마지막 항 삭제
    del match_point[-1]

# 출력시 십의자리가 0일 경우 일의자리만 출력해야하므로 번거롭지만 정수로 변환후 다시 문자열 형태로 출력하였다.
end_point = str(int(str(int(match_point[0])) + str(int(match_point[1]))))+"%"
print(end_point)


# **다른사람의 풀이**
# 내 코드길이가 이 코드길이보다 3배나 길다.

# map(): list나 dictionary같이 iterable한 데이터를 인자로 받아 list안의 개별 아이템을 함수의 인자로 전달하여 결과를 리스트로 전달함
# 간단히 map()함수를 이용하여 입력받은 값 정수로 변환

N, M = map(int, input().split())
A, B = input().split()
alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

AB = ''
min_len = min(N, M)

# 이렇게 하면 나처럼 A > B, A = B, A < B 총 세 가지의 조건으로 나누지 않고도 짧게 A와 B를 합칠 수 있다.
for i in range(min_len):
  AB += A[i] + B[i]
AB += A[min_len:] + B[min_len:]

# ord(): 문자의 아스키 값을 돌려주는 함수
# 아스키 값의 성질을 이용해 알파벳 횟수의 값을 돌려줌. - 아스키 값이 알파벳 순서대로 들어있기 때문에
# 아스키 값의 성질을 이용해서 따로 나처럼 딕셔너리를 이용해 맵핑할 필요가 없음.
lst = [alp[ord(i) - ord('A')] for i in AB]

for i in range(N + M - 2):
  # 반복할 때마다 1씩 줄어드므로 i만큼 빠진다.
  for j in range(N + M - 1 - i):
    lst[j] += lst[j+1]

# format()을 이용하여 간단하게 숫자를 %가 붙은 문자열로 출력할 수 있다.
# 이걸보고 깨달았다. 나처럼 매번 연산마다 일의 자리만 저장할 필요 없이 최종 출력 때만 10으로 나눠주면 됐다...!
print("{}%".format(lst[0] % 10 * 10 + lst[1] % 10))
