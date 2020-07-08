'''
	Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
	Example:
	Input: [-2,1,-3,4,-1,2,1,-5,4],
	Output: 6
	Explanation: [4,-1,2,1] has the largest sum = 6.
'''
def maxSubarray(num_list):
    if not sum:
        return 0
    currSum, result = num_list[0], num_list[0]
    n = len(num_list)
    for index in range(1, n):
        currSum = max(num_list[index], currSum+num_list[index])
        result = max(result, currSum)
    return result