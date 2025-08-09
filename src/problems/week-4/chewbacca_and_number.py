x = list(map(int, list(input())))

for i in range(len(x)):
  if x[i] >= 5:
    if 9 - x[i] == 0 and i == 0:
      continue
    x[i] = 9 - x[i]
  
print("".join(list(map(str, x))))
