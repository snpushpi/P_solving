'''
	Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
	Note: You can only move either down or right at any point in time.
'''
def min_path_sum(grid):
    if not grid:
        return 0
    row, col = len(grid), len(grid[0])
    dp = [[0 for i in range(col)] for j in range(row)]
    dp[0][0] = grid[0][0]
    for i in range(row):
        dp[row][0]=dp[row-1][0]+grid[row][0]
    for j in range(col):
        dp[0][col]=dp[0][col-1]+grid[0][col]
    for i in range(row):
        for j in range(col):
            dp[i][j]=min(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j])
    return dp[row-1][col-1]
