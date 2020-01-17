def end_other(a, b):
  if len(a) == len(b):
    return a == b
  mn = min(len(a), len(b))
  long_string = ''
  short_string = ''
  long_string = a if len(a)>len(b) else b
  short_string = a if len(a)<len(b) else b
  return short_string.lower() == long_string.lower()[-mn:]
