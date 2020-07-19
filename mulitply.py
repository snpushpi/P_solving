'''
	Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
	Example 1:
	Input: [2,3,-2,4]
	Output: 6
	Explanation: [2,3] has the largest product 6.
	Example 2:
	Input: [-2,0,-1]
	Output: 0
	Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
def multiply_list(num_list):
    l = len(num_list)
    dp = [0 for i in range(l)]
    dp[0]=num_list[0]
    for i in range(1,l):
        dp[i]=max(dp[i-1]*num_list[i], num_list[i])
    maximum = 0
    for i in range(l):
        if dp[i]>maximum:
            maximum = dp[i]
    return maximum