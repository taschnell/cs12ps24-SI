#include <iostream>
int x = 1;

int main() {
  for (int i = 0; i < 10; ++i) {
    if (i > 5) {
      continue;
    }
      else {
        std::cout << i;
      }
    
  }
}