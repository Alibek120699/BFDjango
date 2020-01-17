def front_back(str):
  n = len(str)-1
  if not n>0:
    return str
  new_str = str[1:n]
  return str[-1]+new_str+str[0]
