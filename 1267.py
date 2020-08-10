'''
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
Return the number of servers that communicate with any other server.
Example 1:
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
'''
def main(grid):
    col_dict = {}
    row_dict = {}
    row_num = len(grid)
    col_num = len(grid[0])
    for row in range(row_num):
        for col in range(col_num):
            if grid[row][col]==1:
                if row not in row_dict:
                    row_dict[row]=1
                else:
                    row_dict[row]+=1
                if col not in col_dict:
                    col_dict[col]=1
                else:
                    col_dict[col]+=1
    result =0
    count1, count2=0,0
    temp_row=set()
    temp_col=set()
    for elt in row_dict:
        if row_dict[elt]>=2:
            result+=row_dict[elt]
            count1+=1
            temp_row.add(elt)
    for elt in col_dict:
        if col_dict[elt]>=2:
            result+=col_dict[elt]
            count2+=1
            temp_col.add(elt)
    count = count1*count2
    for row in temp_row:
        for col in temp_col:
            if grid[row][col]!=1:
                count-=1
    return result-count
print(main([[1,0],[1,1]]))
