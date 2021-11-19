# https://programmers.co.kr/learn/courses/30/lessons/72410

# 나의 풀이: 멸망했다...ㅋ

def solution(new_id):

    answer = new_id.lower()
    answer = remove_unavailable_asterisk(answer)
    answer = is_side_point(answer)
    answer = is_null(answer)
    answer = is_multiple_points(answer)
    answer = is_available_length(answer)
    
    return answer


def is_null(string):
    if not string:
        return 'a'
    return string

def remove_unavailable_asterisk(string):
    removed_string = ''
    possible_asterisk = ['-', '_', '.']
    
    for char in string:
        if char.isalnum() or char in possible_asterisk:
            removed_string += char
    return removed_string

def is_multiple_points(string):
    while '..' in string:
        string = string.replace('..', '.')
    return string

def is_side_point(string):
    while string and string[-1] == '.':
        string = string[:-1]

    while string and string[0] == '.':
        string = string[1:]
    return string

def is_available_length(string):
    string = is_long(string)
    string = is_short(string)
    return string

def is_long(string):
    MAXIMUM_LENGTH = 15  
    if len(string) > MAXIMUM_LENGTH:
        string = string[:MAXIMUM_LENGTH]
        string = is_side_point(string)
    return string

def is_short(string):
    MIN_LENGTH = 3
    while len(string) < MIN_LENGTH:
        string += string[-1]
    return string
  
# 다른 사람의 풀이
# 정규식의 끝판왕을 봐버렸다...
# 끝장 났다...
import re

def solution2(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
