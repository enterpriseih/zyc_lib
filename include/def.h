class no_assign {
  void
  operator=(const no_assign &) = delete; // 通过delete关键字来实现禁止赋值操作符
};

class no_copy {
  void no_copy(const no_copy &); // 通过只声明而不实现的方式实现禁止copy构造函数
};
