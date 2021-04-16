# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577

# 첫 번째 시도 - 시간 초과 !!
# 글자 수로 정렬하면 편할 거라고 생각했었다
def solution(phone_book):
    phone_book = sorted(phone_book, key=len)
    
    while phone_book:
        num = phone_book.pop(0)
        for phone_num in phone_book:
            if phone_num.startswith(num):
                return False
            else:
                continue
    return True
  
# 다음 시도
# 그냥 정렬을 할 경우에 앞의 글자 순서대로 정렬된다..!
# 그래서 앞뒤 값만 비교해주면 되는 것.
def solution(phone_book):
  phone_book = sorted(phone_book)
  for i in range(len(phone_book) - 1):
      if phone_book[i + 1].startswith(phone_book[i]):
          return False
  return True
  
# 다른 사람의 풀이
# zip을 이용한 풀이로 비교를 용이하게 해준다.
def solution(phoneBook):
  phoneBook = sorted(phoneBook)

  for p1, p2 in zip(phoneBook, phoneBook[1:]):
      if p2.startswith(p1):
          return False
  return True
# hash 를 이용한 풀이
def solution(phone_book):
  answer = True
  hash_map = {}
  for phone_num in phone_book:
    hash_map[phone_num] = 1
  for phone_num in phone_book:
    temp = ""
    for num in phone_num:
      temp += num
      if temp in hash_map and temp != phone_num:
        answer = False
   return answer
