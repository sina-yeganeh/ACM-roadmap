n = int(input())
xi = list(map(int, input().split()))

# 3 10 8 6 11
xi.sort()
# 3 6 7 8 10 11

# m = 9

q = int(input())
for _ in range(q):
  m = int(input())
  start = 0
  end = n - 1
  number = 0
  while start <= end:
    mid = (start + end) // 2

    if xi[mid]:
      number = m
    elif xi[mid] > m:
      pass
