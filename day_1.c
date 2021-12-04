#include <stdio.h>

int process_one(int vals[], int sze) {
  int r = 0;
  for (int i = 1; i < sze; i++) {
    if (vals[i] > vals[i-1]) ++r;
  }
  return r;
}

int process_two(int vals[], int sze, int rng) {
  int r = 0;
  unsigned long int a, b;
  for (int i = rng; i < sze; i++) {
    a = 0;
    b = 0;
    for (int j = 0; j < rng; j++) {
      a += vals[i-j];
      b += vals[i-j+1];
    }
    if (b > a) ++r;
  }
  return r;
}
