'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?
Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[2,3]
''' 
def main(num_list):
    result = []
    for i,num in enumerate(num_list):
        if num<0:
            index = -num-1
        else:
            index = num-1
        if num_list[index]<0:
            
            result.append(index+1)
        num_list[index]*=-1
    return result
print(main([4,3,2,7,2,8,3,1]))