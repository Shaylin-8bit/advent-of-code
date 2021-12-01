#include <stdio.h>

void parse(char* input, char* output) {
  FILE* inptr = fopen(input, "r");
  FILE* outptr = fopen(output, "w");
  char c;

  fputs("{ ", outptr);

  while ((c = getc(inptr)) != EOF) {
    c != '\n' ? putc(c, outptr) : fputs(",\n  ", outptr);
  }
  
  fputs("\n}", outptr);

  fclose(inptr);
  fclose(outptr);
}
