#include <fcntl.h>
#include <stdio.h>
#include <sys/mman.h>
#include <unistd.h>

int main(int argc, char **argv) {
  if (argc != 2) {
    printf("usage: ./a.out filename");
    return 0;
  }
  char *file_name = argv[0];
  printf("copy file: %s", file_name);
  int file = open(file_name, O_RDONLY);
  size_t file_size = lseek(file, 0, SEEK_END);
  printf("file bytes: %lu", file_size);
  void *buffer = mmap(NULL, file_size, PROT_READ, MAP_FILE, file, 0);
  write(1, buffer, file_size);
  return 0;
}
