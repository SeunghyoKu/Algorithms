# 나의 풀이

def solution(s):
    answer = ''
    numbers_english = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    curr = ''
    
    for i in s:
        if i.isalpha():
            curr += i
            if curr in numbers_english:
                answer += str(numbers_english.index(curr))
                curr = ''
        else:
            answer += i
        
    return int(answer)
  
  ### 다른 사람의 풀이
  
  num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
