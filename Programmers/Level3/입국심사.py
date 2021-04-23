# 입국심사 - 이분탐색

# 첫번째 시도한 것
# ㅋㅋㅋ 하나하나 다 넣어서 하나하나 검사하기 -> 당연히 시간 초과가 났다.
def solution(n, times):
    answer = 0
    if len(times) == 1:
        return n * times[0]
    if n == 0:
        return 0
    
    start = times[0]
    end = n * times[len(times) - 1]
    answer = binary_search(times, n, start, end)
    return answer

def binary_search(times, n, start, end):
    mid = (start + end) // 2
    arr = []
    for i in range(len(times)):
        for j in range(1, (n + 1)):
            arr.append(times[i] * j)
    result = sorted(arr)[:n][-1]
    return result

# 문열어!!
# 두번째로 한 풀이 - 정석적으로 dp를 이용해서 풀어보기로 했다
def solution(n, times):
    answer = 0
    if len(times) == 1:
        return n * times[0]
    if n == 0:
        return 0
    
    times.sort()
    start = times[0]
    end = n * times[len(times) - 1]
    answer = binary_search(times, n, start, end, answer)
    return answer

def binary_search(times, n, start, end, answer):
    while start <= end:
        mid = (start + end) // 2
        people = 0
        for i in range(len(times)):
            people += mid // times[i]

        if people >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer
