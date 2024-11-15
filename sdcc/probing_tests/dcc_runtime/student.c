// #include <stdio.h>
// #include <stdlib.h>
//
// int main(int argc, char *argv[]) {
//   printf("hello from student.c\n");
//   char **a = (char **)malloc(2 * sizeof(char));
//   a[argc] = NULL;
//   printf("should error: %d\n", **a);
//   return 0;
// }

#include <stdio.h>

struct list_node {
    struct list_node *next;
    int data;
};

int main(void) {
  struct list_node s = {0};
  struct list_node *a = &s;
  while (a != NULL) {
    a->next->data = 42;
    a = a->next;
  }
}

//int main(int argc, char *argv[]) {
//    struct list_node s1, s2 = { 0 };
//    struct list_node *a = &s1;
//    s1.next = &s2;
//    a->next->next->data = 42;
//}
