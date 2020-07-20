'''
Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)
Return the largest possible sum of the array after modifying it in this way.
 
Example 1:
Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].
Example 2:
Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
Example 3:
Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
'''
def min_index(num_list):
    minima = float('inf')
    index =0
    for i in range(len( num_list)):
        if num_list[i]<minima:
            minima=num_list[i]
            index=i
    return index
def largest_sum(num_list,k):
    for i in range(k,0,-1):
        index = min_index(num_list)
        num_list[index]=-num_list[index]
    sum = 0
    for elt in num_list:
        sum+=elt 
    return sum
print(largest_sum([3,-1,0,2],1))