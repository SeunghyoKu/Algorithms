def solution(s):
    splitted = s.split(' ')
    for i in range(len(splitted)):
        splitted[i] = splitted[i].capitalize()
    return " ".join(splitted)
