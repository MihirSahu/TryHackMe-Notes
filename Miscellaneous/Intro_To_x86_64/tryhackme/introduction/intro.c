#include <stdio.h>

int main(void){
  int a = 1;
  int b = 2;
  int z = 0;
  printf("value for a is %d and b is %d\n", a, b);
  z = b;
  b = a;
  a = z;
  printf("value of a is %d and b is %d\n", a, b);
}
