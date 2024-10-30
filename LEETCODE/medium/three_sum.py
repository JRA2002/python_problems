'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.'''

def find_sum(nums: list):
         
    nums.sort()
    i = 0
    n = len(nums)
    j = n - 1
    ans = []
    idx = {}
    for k in range(n):
        if nums[k] in idx:
            idx[nums[k]] = k
        idx[nums[k]] = k
    print(idx)
    
    while i <= j:
        res = (nums[i]+nums[j])
    
        if -res in nums and i != j:
                ans.append([nums[i],nums[j],-res])
                i += 1
                j -= 1
        elif res > 0:
            j -= 1
        else:
            i += 1
    
    return ans
nums = [-1,0,1,2,-1,-4]
res = find_sum(nums)
print(res)
