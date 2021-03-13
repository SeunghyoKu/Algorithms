# Dongbin Book 3장: 그리디
# 큰 수의 법칙

# solution 1
n, m, k = map(int, input().split(" "))
data = list(map(int, input().split(" ")))
data.sort(reverse=True)
answer, count = 0, 0

for i in range(m):
  if count == k:
    answer += data[1]
    count = 0
  else:
    answer += data[0]
    count += 1

print(answer)

# solution 2
n, m, k = map(int, input().split(" "))
data = list(map(int, input().split(" ")))
data.sort(reverse=True)
first, second = data[0], data[1]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)
