#include <iostream>
#include <unistd.h>
using namespace std;

int x = 1;
int main() {
  if (fork() == 0) {
    printf("p1: x=%d\n", ++x);
  }
  printf("p2: x=%d\n", --x);
  return 0;
}
