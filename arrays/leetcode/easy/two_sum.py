'''Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
 and you may not use the same element twice.

You can return the answer in any order.'''

def two_sum(nums, target):
    
    k = 2
    while k <= len(nums):
        for i in range(len(nums) - k + 1):
            new = nums[i:k+i]
            print(new)
            suma = new[0] + new[-1]
            if suma == target:
                return [i, k+i-1]
        k += 1

nums = [3,3]
target = 6
res = two_sum(nums, target)
print(res)