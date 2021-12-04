#include <stdio.h>

int process_one(char* ctx[], unsigned long sze) {
  int d = 0, h = 0;
  for (int i = 0; i < sze; i++) {
    switch (ctx[i][0]) {
      case 'f':
        h += ctx[i][8] - '0';
        break;
      case 'd':
        d += ctx[i][5] - '0';
        break;
      case 'u':
        d -= ctx[i][3] - '0';
    }
  }
  return d * h;
}

int process_two(char* ctx[], unsigned long sze) {
  int d = 0, h = 0, a = 0;
  for (int i = 0; i < sze; i++) {
    switch (ctx[i][0]) {
      case 'f':
        h += ctx[i][8] - '0';
        d += (ctx[i][8] - '0') * a;
        break;
      case 'd':
        a += ctx[i][5] - '0';
        break;
      case 'u': 
        a -= ctx[i][3] - '0';
    }
  }
  return d * h;
}
