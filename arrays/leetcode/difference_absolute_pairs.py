'''Given an integer array nums and an integer k, return the 
number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.'''
from collections import defaultdict
def absolute_difference(nums: list, k):
    nums.sort()
    i = 0
    j = len(nums) - 1
    count = 0
    while i < j:
        diff = abs(nums[j] - nums[i])
        if diff == k:
            count += 1
        elif diff < k:
            i += 1
        else:
            j -= 1
    
    return count

nums = [1,2,2,1]
k = 1
res = absolute_difference(nums, k)
print(res)