// array_static_illegal_index.c

// int main(void) {
//     int a[5];
//     a[5] = 0;
//     return 0;
// }

// int main(int argc, char *argv[]) {
//   int i = 6.7;
//   return i;
// }

// #include <assert.h>
//
// int main(void) {
//     int i = 10
//     assert(i == 10);
// }

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

// --

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

// --

//int main(int argc, char *argv[]) {
//    struct list_node s1, s2 = { 0 };
//    struct list_node *a = &s1;
//    s1.next = &s2;
//    a->next->next->data = 42;
//}

// --

// #include <stdio.h>
//
// int main(void) {
//   int numbers[10];
//   for (int i = 1; i < 10; i++) {
//     numbers[i] = i;
//   }
//   printf("%d\n", numbers[0]);
// }
