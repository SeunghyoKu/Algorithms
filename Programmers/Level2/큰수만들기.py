# 큰 수 만들기 - 그리디 알고리즘
# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()  
        stack.append(num)
        
    return ''.join(stack[:len(stack) - k])

# 문자열로 풀려고 했는데 이런 문제는 역시 stack을 이용해서 푸는 것이 정답인 것 같다.
# 마지막 return할 때 slicing 해주는 이유는
# 제거 횟수가 남았을 경우에 뒷 부분을 자르기 위해서이다. (12번 케이스에서 걸린다...)

# 12번 테스트케이스는 같은 숫자가 반복될 경우인데
# 입력값: "1111111111", 3 && 기댓값: "1111111" 인 경우이다.
# pop 되지 않고 모두 append 되기에 길이가 원했던 것보다 더 길게 나올 것이다.
# 이럴 경우를 대비해 뒷 부분을 잘라주게 된다.
