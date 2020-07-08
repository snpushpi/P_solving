'''
	You are climbing a stair case. It takes n steps to reach to the top.
	Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
	Note: Given n will be a positive integer.
	Example 1:
	Input: 2
	Output: 2
	Explanation: There are two ways to climb to the top.
	1. 1 step + 1 step
	2. 2 steps
'''
def climbstairs(n):
    dp = [0]*n
    dp[0], dp[1]=1, 2
    for i in range(2,n):
        dp[i]=dp[i-2]+dp[i-1]
    return dp[n-1]
    