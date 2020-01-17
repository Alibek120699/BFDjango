def combo_string(a, b):
  mn=''
  mx=''
  mn = a if len(a)<len(b) else b
  mx = a if len(a)>len(b) else b
  return mn+mx+mn
