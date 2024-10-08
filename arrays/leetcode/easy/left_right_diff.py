'''Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return the array answer.'''

def left_right_diff(nums):
    left_nums = 0
    right_nums = sum(nums)
    ans = []
    i = 0
   
    while i < len(nums):
        right_nums -= nums[i]
        diff = abs(left_nums - right_nums)
        ans.append(diff)
        left_nums += nums[i]

        i += 1
    return ans
nums = [10,4,8,3]

res = left_right_diff(nums)
res = sorted(nums)
print(res)