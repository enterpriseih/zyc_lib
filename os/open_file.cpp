#include <iostream>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>
using namespace std;
//  O_RDRW才会输出, 因为有io，父进程要wait子进程
int main() {
  int fd = open("tmp", O_RDWR|O_APPEND|O_CREAT); 
  pid_t pid = fork();
  if (pid == 0) {
    cout << "this is child process" << endl;
    cout << "fd is: " << fd << endl;
    write(fd,"aaaaaaaa",4);
    close(fd);
  } else {
    wait(NULL);
    cout << "this is parent process" << endl;
    cout << "fd is: " << fd << endl;
    write(fd,"b",1);
  }

  return 0;
}

