t = int(input())

for _ in range(t):
  n, k = list(map(int, input().split()))

  counter = 0
  i = 1
  while counter < k:
    if i % n != 0:
      counter += 1

    i += 1

  print(i - 1)