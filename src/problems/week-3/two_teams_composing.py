t = int(input())

for _ in range(t):
  n = int(input())
  ai = list(map(int, input().split()))

  ai.sort()

  numbers = []
  sub_n = [ai[0]]
  lens = []
  for i in range(1, n):
    if ai[i] != ai[i - 1]:
      numbers.append(sub_n)
      lens.append(len(sub_n))
      sub_n = []

    sub_n.append(ai[i])

  numbers.append(sub_n)
  lens.append(len(sub_n))

  max_len = max(lens)
  numbers_c = numbers.copy()