'''
Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.
Note that the subarray needs to be non-empty after deleting one element.
 
Example 1:
Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
Example 2:
Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.
Example 3:
Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.
 
Constraints:
1 <= arr.length <= 10^5
-10^4 <= arr[i] <= 10^4
'''
def main(num_list):
    l = len(num_list)
    forward_index=[0]*l
    backward_index=[0]*l
    backward_index[l-1]=num_list[l-1]
    forward_index[0]=num_list[0]
    curr_max = -float('inf')
    for i in range(1,l):
        forward_index[i]= max(num_list[i],forward_index[i-1]+num_list[i])
        max_so_far = max(curr_max,forward_index[i])
    for i in range(l-2,-1,-1):
        backward_index[i]=max(num_list[i],backward_index[i+1]+num_list[i])
    result = max_so_far
    for index in range(1,l-1):
        result = max(result,forward_index[index-1]+backward_index[index+1])
    return result
print(main([-1,-1,-1,-1]))