#include <iostream>
#include <memory>
using namespace std;

// 关于shared_ptr的一些测试:
// 1.shared_ptr支持指定自定义的deleter，且其copy 构造函数会copy deleter
// 2.use_cout记录其引用计数
// 3.通过unique ptr构造一个shared ptr会清空原来的unique_ptr

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

void test3() {
  std::unique_ptr<int> unique = std::make_unique<int>(new int(100));
  std::shared_ptr<int> shared(unique);
  if (unique.get() == nullptr) {
    cout << "construct a shared ptr by unique will clear the origin unique ptr"
         << endl;
  }
}

int main() {
  test3();
  return 0;
}
