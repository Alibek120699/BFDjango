def round10(num):
  if num % 10 >= 5:
    return num + 10 - (num % 10)
  return num - (num % 10)
  
def round_sum(a, b, c):
  res = 0
  nums = [a, b, c]
  for i in nums:
    res += round10(i)
  return res
  
