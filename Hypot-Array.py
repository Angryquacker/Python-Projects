from math import *
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums.sort()

for x in nums:
  if x <= len(nums) - 2:
    print hypot(nums[x], nums[x - 1])
  elif x <= len(nums) - 1:
    print "end"
