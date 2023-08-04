#include <iostream>
#include <unistd.h>
using namespace std;

int main() {
  int fds[2];
  int p = pipe(fds);
  pid_t child_write= fork();
  if (child_write == 0) {
    cout << "in write child";
    char c = 'a';
    while(1) {
      write(fds[1], &c, 1);
      c += 1;
    }
  }
  pid_t child_read = fork();
  if (child_read == 0) {
    cout << "in read child";
    while(1) {
     char c;
     read(fds[0], &c, 1);
     cout << "read c is: " << c << endl;
   }
  }
  wait(NULL);
  return 0;
}
