'''Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
 and you may not use the same element twice.

You can return the answer in any order.'''

def two_sum(nums: list, target: int):
    
    k = 2
    while k <= len(nums):
        for i in range(len(nums) - k + 1):
            new = nums[i:k+i]
            suma = new[0] + new[-1]
            if suma == target:
                return [i, k+i-1]
        k += 1
    return []

#optimal approach

def two_sum2(nums: list, target: int):
    mapa = {}
    for i in range(len(nums)):
            mapa[nums[i]] = i
    
    for i in range(len(nums)):
        if target-nums[i] in mapa and mapa[target-nums[i]] != i:
            return [i, mapa[target-nums[i]]]
    return []


nums = [-1,-2,-3,-4,-5]
target = -8

res = two_sum2(nums, target)
print(res)