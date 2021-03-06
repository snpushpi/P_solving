'''
	You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
	Example 1:
	coins = [1, 2, 5], amount = 11
	return 3 (11 = 5 + 5 + 1)
	Example 2:
	coins = [2], amount = 3
	return -1.
'''
def main(coins, amount):
    dp=[-1]*(amount+1)
    dp[0]=0
    for i in range(1,amount+1):
        dp[i]=float('inf')
        for coin in coins:
            if coin<=i:
                dp[i]=min(dp[i],dp[i-coin]+1)
    if dp[amount]==float('inf'):
        return -1
    else:
        return dp[amount]
print(main([1,2,5],11))