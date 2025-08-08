n = int(input())
ai = list(map(int, input().split()))

worms = {}
counter = 0
for i in range(n):
  worms[i] = [j for j in range(counter + 1, counter + ai[i] + 1)]
  counter += ai[i]

m = int(input())
qi = list(map(int, input().split()))

for q in qi:
  for i in range(n):
    if q in worms[i]:
      print(i + 1)
