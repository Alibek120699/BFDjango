def last2(str):
  if len(str)<2:
    return 0
  subs = str[-2:]
  res = 0
  for i in range(len(str)-2):
    if str[i:i+2] == subs:
      res -=- 1
  return res