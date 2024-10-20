'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.'''

def remove_duplicates(nums: list):
    # we store the unique elements in res
    res = []
    for num in nums:
        if num not in res:
            res.append(num)
    # iterate over nums
    i = 0
    j = 0
    n = len(nums) - 1
    while i <= n and j <= len(res) - 1:
        if nums[i] == res[j]:
            nums[i], nums[j] = nums[j], nums[i] #swap if nums[i] equal to res[j]
            i += 1
            j += 1
        else:
            i += 1
        
    return len(res)

# OTHER APPROACH using less memory

def remove_duplicates2(nums: list):
    j = 1
    n = len(nums)
    for i in range(1, n):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1
    return j

nums = [1,1,2]

res = remove_duplicates(nums)
print(res)