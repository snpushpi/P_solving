'''
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
 
Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''
def main(input_list):
    i,j=0,0
    for elt in input_list:
        if elt<=0:
            i+=1
    if i>0:
        j=i
        i-=1
    print(i,j)
    result_list = []
    while i>=0 and j<=len(input_list)-1:
        if input_list[i]**2<input_list[j]**2:
            result_list.append(input_list[i]**2)
            i-=1
        elif input_list[i]**2>input_list[j]**2:
            result_list.append(input_list[j]**2)
            j+=1
        else:
            result_list.append(input_list[i]**2)
            i-=1
            j+=1
    while i>=0:
        result_list.append(input_list[i]**2)
        i-=1
    while j<=len(input_list)-1:
        result_list.append(input_list[j]**2)
        j+=1
    return result_list
print(main([3,10]))

