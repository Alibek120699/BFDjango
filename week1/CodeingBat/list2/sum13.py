def sum13(nums):
  if len(nums) == 0:
    return 0
  res = 0 if nums[0] == 13 else nums[0]
  for i in range(1, len(nums)):
    if nums[i] == 13:
      continue
    if nums[i-1] == 13:
      continue
    res += nums[i]
  return res
