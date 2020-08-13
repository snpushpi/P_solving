'''
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.
Example:
For the given grid
0 E 0 0
E 0 W E
0 E 0 0
return 3. (Placing a bomb at (1,1) kills 3 enemies)
'''
def check(row,col,grid):
    result = 0
    for i in range(col+1,len(grid[0])):
        if grid[row][i]=='E':
            result+=1
        if grid[row][i]=='W':
            break
    for i in range(col-1,-1,-1):
        if grid[row][i]=='E':
            result+=1
        if grid[row][i]=='W':
            break
    for i in range(row-1,-1,-1):
        if grid[i][col]=='E':
            result+=1
        if grid[i][col]=='W':
            break
    for i in range(row+1,len(grid)):
        if grid[i][col]=='E':
            result+=1
        if grid[i][col]=='W':
            break
    return result

def main(grid):
    if len(grid)==0 or len(grid[0])==0:
        return 0
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='0':
               
                result= max(check(i,j,grid),result)
    return result
print(main([['0', 'E', '0', '0'],
['E', '0', 'W', 'E'],
['0', 'E', '0', '0']]))  