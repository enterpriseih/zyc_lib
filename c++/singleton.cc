#include <iostream>

template <typename T> class SingletonBase {
public:
  static T &Instance() { // 1.要提供一个static的访问函数
    static T instance;
    return instance;
  }

protected: // 3.作为模板基类·构造函数需要能够被子类调用
  SingletonBase() {} // 2.将构造函数和拷贝构造函数都设置为private
  SingletonBase(const SingletonBase &s) {}
};

class MySingleton : public SingletonBase<MySingleton> {};

int main() {
  MySingleton::Instance();
  return 0;
}
