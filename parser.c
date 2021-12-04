void parse(char* input, char* output, char t) {
  FILE* inptr = fopen(input, "r");
  FILE* outptr = fopen(output, "w");
  char c;
  // true t val will format as char*, false as int
  fputs((t ? "char* ctx[] = {\n  \"" : "int* ctx = {\n  "), outptr);
  while ((c = getc(inptr)) != EOF) {
    c != '\n' ? putc(c, outptr) : fputs((t ? "\",\n  \"" : ",\n  "), outptr);
  }  
  fputs((t ? "\"\n};" : "\n};"), outptr);

  fclose(inptr);
  fclose(outptr);
}
