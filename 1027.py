'''
Given an array A of integers, return the length of the longest arithmetic subsequence in A.
Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).
 
Example 1:
Input: [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
Example 2:
Input: [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].
'''
def determiner(num_list):
    dp = {}
    l = len(num_list)
    for i in range(l):
        for j in range(i):
            d = num_list[i]-num_list[j]
            dp[(i,d)]=1
    
    for i in range(1,l):
        for j in range(i):
            d = num_list[i]-num_list[j]
            if (j,d) in dp:
                dp[(i,d)]=dp[(j,d)]+1
    print(dp)
    Keymax = max(dp, key=dp.get) 
    return dp[Keymax]+1
print(determiner([3,6,9,12]))
            