n, m = list(map(int, input().split()))

def y_to_x(x, y, steps):
  if y <= x:
    steps += x - y
    return steps

  if y % 2 == 0:
    steps += 1
    return y_to_x(x, y // 2, steps)
  else:
    steps += 1
    y += 1
    return y_to_x(x, y, steps)

print(y_to_x(n, m, 0))