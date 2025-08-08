#include <stdio.h>
#include <math.h>

int is_prime(long long int n) {
  if (n <= 3) {
    return n > 1;
  }
  if (n % 2 == 0) {
    return 0;
  }

  for (int i = 3; i < (int) sqrt(n) + 1; i += 2) {
    if (n % i == 0) {
      return 0;
    }
  }
  return 1;
}

int is_t_prime(long long int n) {
  long long int root = (int) sqrt(n);
  if (root * root != n) {
    return 0;
  }

  if (is_prime(root)) {
    return 1;
  }
  return 0;
}

int main() {
  long int n;
  scanf("%ld", &n);

  for (int i = 0; i < n; i++) {
    long long int number;
    scanf("%lld", &number);

    if (is_t_prime(number)) {
      printf("YES\n");
    } else {
      printf("NO\n");
    }
  }

  return 0;
}