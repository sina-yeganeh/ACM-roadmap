# from itertools import combinations

numbers = list(map(int, input().split()))

n = numbers[0]
numbers.remove(n)

def solve():
  for number in numbers:
    if n % number == 0:
      print(int(number / n))
      return 

  numbers.sort()
  min_n = numbers[0]
  ext = n % min_n
  base_list = [min_n] * (n // min_n)

  while sum(base_list) != n:
    pass