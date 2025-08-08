from math import sqrt

n = int(input())
numbers = list(map(int, input().split()))

def is_prime(n: int):
  if n <= 3:
    return n > 1
  if n % 2 == 0:
    return False
  
  for i in range(3, int(sqrt(n)) + 1, 2):
    if n % i == 0:
      return False
  return True

# def creat_prime(n: int):
#   primes = []
#   for i in range(0, n):
#     pass

def is_t_primes(n: int):
  root = int(sqrt(n))
  if root ** 2 != n:
    return False
  
  if is_prime(root):
    return True
  return False

for number in numbers:
  if is_t_primes(number):
    print("YES")
  else:
    print("NO")
