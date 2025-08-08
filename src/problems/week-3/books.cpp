#include <iostream>
#include <vector>

using namespace std;

int main() {
  long int n;
  long long int t;

  cin >> n >> t;

  vector<long int> books(n);  
  for (int i = 0; i < n; i++) {
    cin >> books[i];
  }

  int max_b = 0;
  for (int i = 0; i < n; i++) {
    int counter = 0;
    long long int book_sum = 0;

    while (i + counter < n && book_sum <= t) {
      book_sum += books[i + counter];
      if (book_sum > t) {
        break;
      }

      counter += 1;
    }

    if (counter > max_b) {
      max_b = counter;
    }
  }

  cout << max_b << endl;

  return 0;
}