def front_times(str, n):
  new_str = ''
  for i in range(n):
    new_str += str[:3]
  return new_str