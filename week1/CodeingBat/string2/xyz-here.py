def xyz_there(str):
  return str.count('xyz', 0, len(str))-str.count('.xyz', 0, len(str))>0
