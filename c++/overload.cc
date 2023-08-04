#include <iostream>
// 对于重载的测试
// 1. 返回值不能用于重载
// 2. const member function不能用于重载
class A {
public:
  void f() {}
  // int f() { return 1; }
  // int &f() { return 1; }
  // int &&f() { return 1; }
  void f(int a) {}
  // int f() {} return value can not overload
  void f() const {} // const member func can overload
  void f(int &&a) {}
};
int main() { return 0; }
