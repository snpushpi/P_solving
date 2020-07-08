'''
	Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
	Example:
	Input: [-2,1,-3,4,-1,2,1,-5,4],
	Output: 6
	Explanation: [4,-1,2,1] has the largest sum = 6.
'''
def largest_subarray(nums):
    current_sum = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i],current_sum+nums[i])
        result = max(result, current_sum)
    return result