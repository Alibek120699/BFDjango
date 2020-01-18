def centered_average(nums):
  res = 0
  for i in nums:
    res += i
  res -= min(nums) + max(nums)
  return res // (len(nums) - 2)
