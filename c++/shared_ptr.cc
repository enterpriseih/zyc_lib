#include <iostream>
#include <memory>
using namespace std;
void test1() {
  std::shared_ptr<int> a = std::make_shared<int>(4);
  std::shared_ptr<int> b = a;
  cout << "before reset: " << endl;
  cout << "a: " << *a << endl;
  cout << "a addr: " << a.get() << endl;
  cout << "b: " << *b << endl;
  cout << "b addr: " << b.get() << endl;
  cout << "a.count" << a.use_count() << endl;
  // b.reset(new int(5));
  b = std::make_shared<int>(5);
  cout << "after reset: " << endl;
  cout << "a: " << *a << endl;
  cout << "a addr: " << a.get() << endl;
  cout << "b: " << *b << endl;
  cout << "b addr: " << b.get() << endl;
  cout << "a.count" << a.use_count() << endl;
}
void test2() {
  auto deletera = [](int *ptr) {
    delete ptr;
    std::cout << "i am the deletera" << endl;
  };
  auto deleterb = [](int *ptr) {
    delete ptr;
    std::cout << "i am the deleterb" << endl;
  };
  shared_ptr<int> a(new int(4), deletera);
  shared_ptr<int> b(new int(3), deleterb);
  cout << "before b=a" << endl;
  b = a; // also copy the deleter
  cout << "after b=a" << endl;
  ;
}

int main() {
  test2();
  return 0;
}
