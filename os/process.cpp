#include <iostream>
#include <unistd.h>
#include <sys/wait.h>
using namespace std;
//  进程间栈数据不共享
int main() {
  int x = 100;
  pid_t pid = fork();
  cout << "pid is: " << pid << endl;
  if (pid == 0) {
    cout << "this is parend process" << endl;
    cout << "in child x is: " << x << endl;
    x = 101;
  } else {
    cout << "this is child process" << endl;
    int status;
    wait(&status);
    cout << "in parent x is: " << x << endl;
    x = 200;
  }
  cout << "-----x is: " << x << endl;
  return 0;
}
