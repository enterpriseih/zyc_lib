#include <iostream>
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
