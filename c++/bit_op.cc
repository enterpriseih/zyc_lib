#include <iostream>
using namespace std;
// 左移 << 相当于 乘以2
// 右移 >> 相当于除以2
int main() {
  int a = -2;
  a >>= 1;
  cout << a << endl;
  return 0;
}
