'''
    You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
    Example:
    Given nums = [5, 2, 6, 1]
    To the right of 5 there are 2 smaller elements (2 and 1).
    To the right of 2 there is only 1 smaller element (1).
    To the right of 6 there is 1 smaller element (1).
    To the right of 1 there is 0 smaller element.
    Return the array [2, 1, 1, 0].
'''
def binary_search(array,target):
    low, high = 0, len(array)-1
    while low<=high:
        mid = (low+high)//2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            low = mid+1
        elif array[mid]>target:
            high = mid-1
    

import bisect
def binary_insert(array,target):
    bisect.insort(array,target)
    return array
def main(array):
    temp_array = [array[-1]]
    result = []
    l = len(array)
    for i in range(l-2,-1,-1):
        temp_array = binary_insert(temp_array,array[i])
        result.append(binary_search(temp_array,array[i]))
    result.reverse()
    return result+[0]
print(main([98,8,7,100,9]))
        

