#include <iostream>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>
using namespace std;
// 关闭标准输出，则不会输出
int main() {
  pid_t pid = fork();
  if (pid == 0) {
    cout << "this is child process" << endl;
    //close(STDOUT_FILENO);
    printf("this is child out");
  } else {
    cout << "this is parent process" << endl;
  }
  return 0;
}


