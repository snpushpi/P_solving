'''
Given an integer array A, you partition the array into (contiguous) subarrays of length at most K.  After partitioning, each subarray has their values changed to become the maximum value of that subarray.
Return the largest sum of the given array after partitioning.
 
Example 1:
Input: A = [1,15,7,9,2,5,10], K = 3
Output: 84
Explanation: A becomes [15,15,15,9,10,10,10]
 
Note:
1 <= K <= A.length <= 500
0 <= A[i] <= 10^6
'''
def maxSumPartioning(A,K):
    N = len(A)
    dp = [0]*(N+1)
    for index_i in range(N):
        max_i = 0
        for index_j in range(index_i, index_i-K, -1):
            if index_j>=0 and index_j<N:
                max_i = max(max_i,A[index_j])
                dp[index_i+1]=max(dp[index_i+1],max_i*(index_i-index_j+1)+dp[index_j])
    print(dp)
    return dp[-1]
print(maxSumPartioning([1,15,7,9,2,5,10],3))