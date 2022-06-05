#include <iostream>
#include <setjmp.h>
using namespace std;
jmp_buf buf;
void foo() {
  cout << "foo()" << endl;
  longjmp(buf, 1);
}
void bar() {
  cout << "bar()" << endl;
  longjmp(buf, 2);
}
int main(int argc, char **argv, char **envp) {
  int i = 0;
  while (envp[i] != nullptr) {
    cout << envp[i] << endl;
    i++;
  }
  switch (setjmp(buf)) {
  case 0: {
    foo();
    break;
  }
  case 1: {
    cout << "long jump 1" << endl;
    bar();
    break;
  }
  case 2: {
    cout << "long jump 2" << endl;
    break;
  }
  }
}
