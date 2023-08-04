#include <iostream>

// test for rvo(return value optimization)
// 减少copy，直接在调用者处构造对象
class A {
public:
  A() { std::cout << "constructor A" << std::endl; }
  ~A() { std::cout << "destructor A" << std::endl; }
  A(const A &a) { std::cout << "copy constructor A" << std::endl; }
};

A GetA() {
  A a;
  return a;
}
int main() {
  A b = GetA();
  return 0;
}
