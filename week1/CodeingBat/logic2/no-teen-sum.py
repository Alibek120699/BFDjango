def no_teen_sum(a, b, c):
  teens = [13, 14, 17, 18, 19]
  if a in teens and b in teens and c in teens:
    return 0
  if a in teens and b in teens:
    return c
  if a in teens and c in teens:
    return b
  if b in teens and c in teens:
    return a
  if a in teens:
    return b + c
  if b in teens:
    return a + c
  if c in teens:
    return a + b
  return a + b + c
