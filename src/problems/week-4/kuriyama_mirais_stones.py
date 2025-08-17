n = int(input())
costs = list(map(int, input().split()))

t = int(input())
for _ in range(t):
  tmp = costs.copy()
  func_type, i, j = list(map(int, input().split()))

  if func_type == 2:
    tmp.sort()

  print(sum(tmp[(i - 1):j]))