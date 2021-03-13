# Dongbin Book - 그리디 알고리즘
# 3. 숫자 카드 게임

n, m = map(int, input().split(" "))
card, min_numbers = [], []

for i in range(n):
  row = list(map(int, input().split(" ")))
  min_numbers.append(min(row))
  card.append(row)

print(max(min_numbers))
