def string_bits(str):
  new_str = ''
  for i in range(0, len(str), 2):
    new_str += str[i]
  return new_str
