'''
Given a 2-dimensional grid of integers, each value in the grid represents the color of the grid square at that location.
Two squares belong to the same connected component if and only if they have the same color and are next to each other in any of the 4 directions.
The border of a connected component is all the squares in the connected component that are either 4-directionally adjacent to a square not in the component, or on the boundary of the grid (the first or last row or column).
Given a square at location (r0, c0) in the grid and a color, color the border of the connected component of that square with the given color, and return the final grid.
Example 1:
Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
Output: [[3, 3], [3, 2]]
Example 2:
Input: grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
Output: [[1, 3, 3], [2, 3, 3]]
Example 3:
Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
Output: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
 
Note:
1 <= grid.length <= 50
1 <= grid[0].length <= 50
1 <= grid[i][j] <= 1000
0 <= r0 < grid.length
0 <= c0 < grid[0].length
1 <= color <= 1000
'''
def colorBorder(grid,r0,c0,color):
    row = len(grid)
    col = len(grid[0])
    visited=[]
    border = []
    def dfs(r,c):
        if r<0 or c<0 or c>=col or r>=row or (r,c) in visited or grid[r][c]!=grid[r0][c0]:
            return
        visited.append((r,c))
        if r==0 or r==row-1 or c==0 or c==col-1 or (r+1<=row-1 and grid[r+1][c]!=grid[r0][c0]) or (r-1>=0 and grid[r-1][c]!=grid[r0][c0]) or (c-1>=0 and grid[r][c-1]!=grid[r0][c0]) or (c+1<=col-1 and grid[r][c+1]!=grid[r0][c0]):
            border.append((r,c))
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)
    dfs(r0,c0)    
    for (x,y) in border:
        grid[x][y]=color
    return grid
print(colorBorder([[1,2,2],[2,3,2]],0,1,3))

        