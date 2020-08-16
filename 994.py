'''
In a given grid, each cell can have one of three values:
the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
'''
def valid(row,col,row_size,col_size):
    return row>0 and row<row_size and col>0 and col<col_size
def main(grid):
    queue = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]==2:
                queue.append((row,col))
    queue.append((-1,-1))#it is a marker of levels
    result = 0
    while queue:
        flag = False
        while (queue[0][0]!=-1 and queue[0][1]!=-1):
            (row,col) = queue[0]
            if valid(row+1,col,len(grid),len(grid[0])) and grid[row+1][col]==1:
                if not flag:
                    flag=True
                    result+=1
                queue.append((row+1,col))
                grid[row+1][col]=2
            if valid(row-1,col,len(grid),len(grid[0])) and grid[row-1][col]==1:
                if not flag:
                    flag = True
                    result+=1
                queue.append((row-1,col))
                grid[row-1][col]=2
            if valid(row,col+1,len(grid),len(grid[0])) and grid[row][col+1]==1:
                if not flag:
                    flag = True
                    result+=1
                queue.append((row,col+1))
                grid[row][col+1]=2
            if valid(row,col-1,len(grid),len(grid[0])) and grid[row][col-1]==1:
                if not flag:
                    flag = True
                    result+=1
                queue.append((row,col-1))
                grid[row][col-1]=2
            queue.pop(0)
        queue.pop(0)
        if queue:
            queue.append((-1,-1))
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]==1:
                return -1

    return result



