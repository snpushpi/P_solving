'''
Given an integer array arr and an integer k, modify the array by repeating it k times.
For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].
Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.
As the answer can be very large, return the answer modulo 10^9 + 7.
 
Example 1:
Input: arr = [1,2], k = 3
Output: 9
Example 2:
Input: arr = [1,-2,1], k = 5
Output: 2
Example 3:
Input: arr = [-1,-2], k = 7
Output: 0
 
Constraints:
1 <= arr.length <= 10^5
1 <= k <= 10^5
-10^4 <= arr[i] <= 10^4
'''
def max_subarray(arr):
    result = -float('inf')
    l = len(arr)
    dp = [0]*l
    dp[0]=arr[0]
    result = dp[0]
    for i in range(1,l):
        dp[i]=max(dp[i-1]+arr[i],arr[i])
        result = max(result,dp[i])
    return result
def main(arr,k):
    l = len(arr)
    if k==1:
        return max_subarray(arr)
    forward_sum=0
    for_max = 0
    for i in range(l):
        forward_sum+=arr[i]
        for_max = max(for_max,forward_sum)
    backward_sum=0
    back_max = 0
    for i in range(l-1,-1,-1):
        backward_sum+=arr[i]
        back_max = max(back_max,backward_sum)
    return max(max_subarray(arr),for_max+back_max,for_max+back_max+(k-2)*forward_sum)
    
print(main([1,-2,1],7))
    