'''
Given a matrix, and a target, return the number of non-empty submatrices that sum to target.
A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.
 
Example 1:
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
 
Note:
1 <= matrix.length <= 300
1 <= matrix[0].length <= 300
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
'''
def submatrices_check(matrix,target):
    row = len(matrix)
    col = len(matrix[0])
    dp = [[0 for i in range(col)] for i in range(row)]
    dp[0][0]=matrix[0][0]
    for i in range(1,row):
        dp[i][0]=dp[i-1][0]+matrix[i][0]
    for i in range(1,col):
        dp[0][i]=dp[0][i-1]+matrix[0][i]
    for i in range(1,row):
        for j in range(1,col):
            dp[i][j]=matrix[i][j]-dp[i-1][j-1]+dp[i-1][j]+dp[i][j-1]
    print(dp)
    result = 0
    for i in range(row):
        for j in range(i+1,row):
            for k in range(col):
                for l in range(k+1,col):
                    check_sum = dp[j][l]-(dp[j][k]+dp[i][l]-dp[i][k])
                    print(check_sum)
                    if check_sum==target:
                        result+=1
    return result
print(submatrices_check([[1,-1],[-1,1]],0))