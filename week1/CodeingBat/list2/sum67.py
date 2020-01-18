def sum67(nums):
  ignore = False
  res = 0
  if len(nums) == 0:
    return 0
  for i in nums:
    if i == 6:
      ignore = True
    if not ignore:
      res += i
    if i == 7:
      ignore = False
  return res
