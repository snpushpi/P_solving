'''
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
 
Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 
Constraints:
1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
'''
def main(matrix):
    row = len(matrix)
    col = len(matrix[0])
    dp = [[0 for i in range(col)] for i in range(row)]
    for i in range(row):
        if matrix[i][0]==1:
            dp[i][0]=1
            
    for i in range(col):
        if matrix[0][i]==1:
            dp[0][i]=1

    for r in range(1,row):
        for c in range(1,col):
            if matrix[r][c]==1:
                dp[r][c]=min(dp[r-1][c-1],dp[r-1][c],dp[r][c-1])+1
    result=0
    for elt in dp:
        result+=sum(elt)
    return result
print(main([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))
