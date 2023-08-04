#include <iostream>
#include <unistd.h>
using namespace std;
// fork 子进程返回0
// 父进程返回子进程的pid
// 进程间的变量彼此不可见
int x = 1;
int main() {
  if (fork() == 0) {
    printf("p1: x=%d\n", ++x);
  }
  printf("p2: x=%d\n", --x);
  return 0;
}
