#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  printf("hello from student.c\n");
  char **a = (char **)malloc(2 * sizeof *a);
  a[argc] = NULL;
  printf("should error: %d\n", **a);
  return 0;
}
