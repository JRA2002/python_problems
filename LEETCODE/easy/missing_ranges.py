"Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges."

def find_ranges(nums: list, lower, upper):
    k = 2
    n = len(nums)
    res = []
    for i in range(n - k + 1):
        print(nums[i+1])
        if nums[i]+1 == nums[k+i-1]:
            continue
        else:
            res.append(nums[i]+1)
        if nums[k+i-1]-1 == nums[i]:
            continue
        else:
            res.append([nums[i]+1,nums[k+i-1]-1])
        
        
    print(res)

nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
res = find_ranges(nums, lower, upper)
print(res)