#include <iostream>
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
