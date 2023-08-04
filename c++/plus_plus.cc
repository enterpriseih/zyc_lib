#include <iostream>
// 后置的++会多一次copy，且一般会调用前置的++
int main() {
  int i = 2;
  // i++ ++;
  // ++ ++i;
  std::cout << ++i;
  int j = 2;
  std::cout << j++;
  return 0;
}
