#include <iostream>
#include <typeinfo>
using namespace std;
//  type_id 标识对象啊的实际类型
class Base {
public:
  virtual ~Base() {} // without this line the class is not polymorphic
};

class SubClass : public Base {};

int main() {
  Base *b = new Base();
  cout << "b is a base class" << endl;
  cout << typeid(*b).name() << endl;
  b = new SubClass();
  cout << "b is a sub class" << endl;
  cout << typeid(*b).name() << endl;
  return 0;
}
