def love6(a, b):
  if a == 6 or b == 6:
    return True
  if a+b == 6:
    return True
  if abs(a-b) == 6:
    return True
  return False