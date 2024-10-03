'''Given an integer array nums, move all 0's to the end 
of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.'''

def move_zeros(nums: list):
        left = 0

        for right in range(len(nums)):
                if nums[right] != 0:
                    nums[right], nums[left] = nums[left], nums[right]
                    left += 1
        return nums

nums = [0,1,0,3,12]
res = move_zeros(nums)
print(res)

# Time Complexity:O(N)
# Auxiliary Space: O(1)