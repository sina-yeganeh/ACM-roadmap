t = int(input())

for _ in range(t):
  n = int(input())
  numbers = list(map(int, input().split()))

  # numbers.sort()

  odds = []
  evens = []
  for number in numbers:
    if number % 2 == 0:
      evens.append(number)
    else:
      odds.append(number)

  if len(odds) % 2 == 0:
    print("YES")
  else:
    numbers.sort()
    flag = False
    for i in range(0, n - 1):
      if numbers[i + 1] - numbers[i] == 1:
        flag = True
        print("YES")
        break

    if not flag:
      print("NO")