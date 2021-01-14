# 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

def solution(numbers, hand):
    answer = []
    left_hand, right_hand = [0, 3], [2,3]
    keypad = [[1, 4, 7], [2, 5, 8, 0], [3, 6, 9]]
      
    def get_index(num):
        return [num, keypad[num].index(number)]

    def use_hand(h, idx):
        answer.append(h)
        if h == 'L':
            return get_index(idx)
        elif h == 'R':
            return get_index(idx)
            
    for number in numbers:
        if number in keypad[0]:
            left_hand = use_hand('L', 0)
        elif number in keypad[2]:
            right_hand = use_hand('R', 2)
        else:
            curr_index = get_index(1)
            left, right = get_distance(left_hand, right_hand, curr_index)
            if left > right:
                right_hand = use_hand('R', 1)
            elif right > left:
                left_hand = use_hand('L', 1)
            else:
                if hand == 'left':
                    left_hand = use_hand('L', 1)
                else:
                    right_hand = use_hand('R', 1)
    return ''.join(answer)

def get_distance(left, right, curr):
    left_dist = abs(left[0] - curr[0]) + abs(left[1] - curr[1])
    right_dist = abs(right[0] - curr[0]) + abs(right[1] - curr[1])
    return left_dist, right_dist
