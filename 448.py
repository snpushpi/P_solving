'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[5,6]
'''
def main(num_list):
    for i,elt in enumerate(num_list):
        if elt<0:
            index = -elt-1
        else:
            index = elt-1
        if num_list[index]>0:
            num_list[index]*=-1
    result = []
    for i in range(len(num_list)):
        if num_list[i]>0:
            result.append(i+1)
    return result
print(main([4,3,2,7,8,2,3,1]))