def string_splosion(str):
  n = len(str)
  new_str = ''
  for i in range(n):
    new_str += str[:i+1]
  return new_str
