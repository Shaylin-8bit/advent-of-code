int process_one(char* ctx[], unsigned long sze) {
  int r=0, s=0, on;
  int l = strlen(ctx[0]);

  for (int i = 0; i < l; i++) {
    on = 0;
    for (int j = 0; j < sze; j++) {
      on += ctx[j][i] - '0';
    }
    if (on > sze/2) {
      r = r | 1 << (l-(i+1));
    } else {
      s = s | 1 << (l-(i+1));
    }
  }
  return r * s;
}
