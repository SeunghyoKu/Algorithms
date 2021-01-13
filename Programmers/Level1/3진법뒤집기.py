# 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935

# 나의 풀이
def solution(n):
    after_divide = divmod(n, 3)
    base3 = [str(after_divide[1])]
    answer = 0
    
    while after_divide[0] > 2:
        after_divide = divmod(after_divide[0], 3)
        base3.insert(0, str(after_divide[1]))
    base3.insert(0, str(after_divide[0]))
    
    # 이 부분은, 몫이 0일 때를 제대로 처리하지 못해 앞에 0이 붙을 수도 있어서 이처럼 처리했다.
    # 조건을 n > 0 과 같이 0을 처리해준다면 뒤에 이런 코드를 추가하지 않아도 좋을 것 같다.
    base3 = str(int(''.join(base3)))[::-1]
    
    for i in range(len(base3)):
        answer += (3 ** (len(base3) - i - 1)) * int(base3[i])
    return answer

'''
그냥 딱 떠오르는 게 divmod여서 풀다보니, 더 좋게 풀이하는 방법에 대해서는 고려하지 못했던 것 같다. :-(
파이썬에서는 3진법을 구현하는 방법이 없어서 (2/8/16진법은 구현되어 있다.) 직접 구현 해야 됐다.

결과적으로는 몫과 나머지만을 구하면 되니, 위처럼 굳이 divmod를 사용하지 않아도 될 듯하다.
직접 10진법 => 3진법 => 반전 => 10진법 과정을 구현해보았다는데 의의를 둔다..

JS로도 풀어보고 싶다.

# 예시
bin(123) | oct(123) | hex(123)
으로 구현할 수 있다.
'''

# 다른 사람의 풀이

def solution(n):
    answer = 0
    cnt = 1
    a = ''
    while n>0:
        a+=str(n%3)
        n = n//3
    for b in range(len(a),0,-1):
        answer += (int(a[b-1])*cnt)
        cnt *= 3
    return answer
    
# 나머지가.. 제일.. 깔끔한 거 같다.. !
