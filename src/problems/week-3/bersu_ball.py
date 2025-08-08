n = int(input())
boys = list(map(int, input().split()))

m = int(input())
girls = list(map(int, input().split()))

boys.sort()
girls.sort()

paris = 0
for i in range(0, n):
  for j in range(0, len(girls)):
    if abs(boys[i] - girls[j]) <= 1:
      paris += 1
      girls.remove(girls[j])
      break

print(paris)