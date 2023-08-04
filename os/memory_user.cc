#include <memory>
#include <unistd.h>

int main(int argc, char* argv[]) {
  int ch;
  int memory_cost = 0;
  int duration = 100;
  while ((ch = getopt(argc, argv, "m:t:")) != -1) {
    switch(ch) {
        case 'm':
          memory_cost = atoi(optarg);
          printf("memory_cost: %d\n", memory_cost);
          break;
        case 't':
          duration = atoi(optarg);
          printf("duration: %d\n", duration);
          break;
        default:
          break;
    }
  }
  int i = 0;
  while(i < duration) {
    char* alloc = (char*)malloc(memory_cost * 1024 * 1024);
    sleep(1);
    ++i;
  }
  return 0;
}
