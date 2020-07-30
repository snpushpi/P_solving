'''
Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i], ..., A[N-1] in clockwise order.
Suppose you triangulate the polygon into N-2 triangles.  For each triangle, the value of that triangle is the product of the labels of the vertices, and the total score of the triangulation is the sum of these values over all N-2 triangles in the triangulation.
Return the smallest possible total score that you can achieve with some triangulation of the polygon.
 
Example 1:
Input: [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.
Example 2:
3 - 7	3 -	7
| / |	| \ |
5 - 4	5 -	4
Input: [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.  The minimum score is 144.
Example 3:
Input: [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.
 
Note:
3 <= A.length <= 50
1 <= A[i] <= 100
'''

def triangulation(num_list):
    n = len(num_list)
    dp = [[0]*n for i in range(n)]
    for diff in range(n):
        for i in range(n):
            #make a check_list 
            if diff>=2:
                check_list=[]
                for elt in range(i,i+diff):
                    check_list.append(elt%n)
                l = len(check_list)
                val = (i+diff)%n
                dp[i][val]=float('inf')
                for k in range(l):
                    dp[i][val]=min(dp[i][check_list[k]]+dp[check_list[k]][val]+num_list[i]*num_list[val]*num_list[check_list[k]],dp[i][val])
            else:
                dp[i][(i+diff)%n]=0
    return dp[0][n-1]
print(triangulation([3,7,4,5]))
            
