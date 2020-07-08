'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
'''
def unique_paths_with_obstacle(grid):
    m = len(grid)
    n = len(grid[0])
    dp =  [[0 for i in range(n)] for i in range(m)]
    if grid[0][0]==1 or grid[m-1][n-1]==1:
        return 0
    for i in range(1,n):
        if grid[0][i]==1:
            dp[0][i]=0
        else:
            dp[0][i]=dp[0][i-1]
    for j in range(1,m):
        if grid[j][0]==1:
            dp[j][0]=0
        else:
            dp[j][0]=dp[j-1][0]
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                dp[i][j]=0
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dp[m-1][n-1]

