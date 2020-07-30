'''
We write the integers of A and B (in the order they are given) on two separate horizontal lines.
Now, we may draw a straight line connecting two numbers A[i] and B[j] as long as A[i] == B[j], and the line we draw does not intersect any other connecting (non-horizontal) line.
Return the maximum number of connecting lines we can draw in this way.
 
Example 1:
Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
Example 2:
Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:
Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2
 
Note:
1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000
'''
def matcher(list1,list2):
    n = len(list1)
    dp = [[0]*len(list1) for i in range(list2)]
    dp[0][0]=1 if list1[0]==list2[0] else 0
    for i in range(1,len(list1)):
        if list1[0]==list2[i]:
            dp[0][i]=1
        else:
            dp[0][i]=dp[0][i-1]
    for i in range(1,len(list2)):
        if list2[0]==list1[i]:
            dp[i][0]=1
        else:
            dp[i][0]=dp[i-1][0]

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j-1]+1,dp[i-1][j])
            else:
                dp[i][j]=max(dp[i][j-1], dp[i-1][j])
    return dp[len(list2)-1][len(list1)-1]

