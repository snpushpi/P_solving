'''
    Given an integer matrix, find the length of the longest increasing path.
    From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
    Example 1:
    nums = [
      [9,9,4],
      [6,6,8],
      [2,1,1]
    ]
    Return 4
'''
def longestsubstring(nums):
    result = 0
    dp = [[0 for i in range(len(nums[0]))] for j in range(len(nums))]
    for row in range(len(nums)):
        for col in range(len(nums[0])):
            result = max(result,dfs(dp,nums,row,col))
    return result
            
def dfs(dp,nums,i,j):
    if dp[i][j]:
        return dp[i][j]
    directions = [[0,-1],[-1,0],[1,0],[0,1]]
    max_depth = 0
    for dx,dy in directions:
        new_x, new_y = i+dx, j+dy
        if (0<=new_x<len(nums) and 0<=new_y<len(nums[0]) and nums[new_x][new_y]<nums[i][j]):
            max_depth = max(max_depth,dfs(dp,nums,new_x,new_y))
    dp[i][j] = max_depth+1
    return dp[i][j]
print(longestsubstring([
      [9,9,4],
      [6,6,8],
      [2,1,1]
    ]))