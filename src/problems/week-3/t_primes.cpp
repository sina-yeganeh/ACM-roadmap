#include <iostream>
#include <math.h>

using namespace std;

int is_prime(int n) {
  if (n <= 3) {
    return n > 1;
  }
  if (n % 2 == 0) {
    return 0;
  }

  for (long int i = 3; i < (int) sqrt(n) + 1; i += 2) {
    if (n % i == 0) {
      return 0;
    }
  }
  return 1;
}

int is_t_prime(long long int n) {
  long long int root = sqrt(n);
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
  cin >> n;

  while (n--) {
    long long int number;
    cin >> number;
    if (is_t_prime(number)) {
      cout << "YES\n";
    } else {
      cout << "NO\n";
    }
  }

  return 0;
}