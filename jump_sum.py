'''
	Say you have an array for which the ith element is the price of a given stock on day i.
	Design an algorithm to find the maximum profit. You may complete at most two transactions.
	Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
	Example 1:
	Input: [3,3,5,0,0,3,1,4]
	Output: 6
	Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
	             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
'''
def jump_sum(num_list):
    #we can have 0,1 or 2 transactions.
    track_list = [[0 for i in range(len(num_list))] for j in range(3)]
    l = len(num_list)
    for i in range(1,3):
        maxdiff = -num_list[0]
        for j in range(1,l):
            track_list[i][j] = max(track_list[i][j-1], maxdiff+num_list[j])
            maxdiff = max(maxdiff, track_list[i-1][j-1]-num_list[j])
    return track_list[2][l-1]
print(jump_sum([3,3,5,0,0,3,1,4]))