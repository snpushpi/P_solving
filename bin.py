'''
Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number (from most-significant-bit to least-significant-bit.)
Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.
Example 1:
Input: [0,1,1]
Output: [true,false,false]
Explanation: 
The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.
Example 2:
Input: [1,1,1]
Output: [false,false,false]
Note:
1 <= A.length <= 30000
A[i] is 0 or 1
'''
def prefixby5(num_list):
    temp_num=num_list[0]
    result_list = []
    if temp_num%5==0:
        result_list.append(True)
    else:
        result_list.append(False)
    for i in range(1, len(num_list)):
        temp_num = 2*temp_num+num_list[i]
        if temp_num%5==0:
            result_list.append(True)
        else:
            result_list.append(False)
    return result_list 
print(prefixby5([1, 0, 1]))