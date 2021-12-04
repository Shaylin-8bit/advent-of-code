def gen_num(ptr):
  r = 0
  l = len(ptr)
  for i in range(l):
    if (ptr[i] == "1"): 
      r |= 1 << (l-(i+1))
  return r

def most_common(ctx, index):
  a = len([ctx[i] for i in range(len(ctx)) if ctx[i][index] == "1"])
  b = len(ctx) - a
  return "1" if a>=b else "0"

def process_two(ctx): # ctx is given as a list of strings
  a = [ctx[i] for i in range(len(ctx)) if ctx[i][0] == most_common(ctx, 0)]
  b = [ctx[i] for i in range(len(ctx)) if ctx[i][0] != most_common(ctx, 0)]
  place = 1
  while (len(a) > 1 and place < len(a[0])):
    a = [a[i] for i in range(len(a)) if a[i][place] == most_common(a, place)]
    place += 1
  place = 1
  while (len(b) > 1 and place < len(b[0])):
    b = [b[i] for i in range(len(b)) if b[i][place] != most_common(b, place)]
    place += 1
  return gen_num(a[0]) * gen_num(b[0])
