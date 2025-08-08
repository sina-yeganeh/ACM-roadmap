n, t = list(map(int, input().split()))
books = list(map(int, input().split()))

max_b = 0
book_sum = 0
left = 0
for i in range(0, n):
  book_sum += books[i]

  while book_sum > t:
    book_sum -= books[left]
    left += 1

  if max_b < i - left + 1:
    max_b = i - left + 1

print(max_b)