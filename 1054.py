'''
In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].
Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.
 
Example 1:
Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:
Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]
 
Note:
1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
'''
def maxfreq(num_list):
    result=[num_list[0]]
    temp_stack=[]
    for elt in num_list[1:]:
        if result[-1]==elt:
            temp_stack.append(elt)
        else:
            result.append(elt)
            if temp_stack:
                if result[-1]!=temp_stack[-1]:
                    temp= temp_stack.pop()
                    result.append(temp)
    return result
print(maxfreq([1,1,1,2,2,2]))
