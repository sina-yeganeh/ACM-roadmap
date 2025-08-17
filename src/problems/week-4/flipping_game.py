n = int(input())
ai = list(map(int, input().split()))

max_ones = 0
for i in range(n):
  tmp = ai.copy()
  tmp[i] = 1 - tmp[i]
  max_ones = max(sum(tmp), max_ones)
  for j in range(i + 1, n):
    tmp[j] = 1 - tmp[j]

    max_ones = max(sum(tmp), max_ones)

# if len(ai) == 1 and ai[0] == 0:
#   print(1)
# else:
print(max_ones)
