def array123(nums):
  return len(set(filter(lambda x: x==1 or x==2 or x==3, nums)))==3
