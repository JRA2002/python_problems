'''Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.'''

def remove_element(nums: list, val: int):
    
    i = 0
    n = len(nums)
    j = n - 1
    while i <= j:
        if nums[i] == val and nums[j] != val:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        elif nums[i] != val:
            i += 1
        elif nums[j] == val:
            j -= 1
    return i

nums = [3]
val = 2

res = remove_element(nums, val)
print(res)