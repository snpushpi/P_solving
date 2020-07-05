'''
	Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
	Your algorithm's runtime complexity must be in the order of O(log n).
	If the target is not found in the array, return [-1, -1].
	Example 1:
	Input: nums = [5,7,7,8,8,10], target = 8
	Output: [3,4]
'''
def finding_nearest_target(num_list, target):
    left, right = 0, len(num_list)-1

    while left<=right:
        mid = int((left+right)/2)
        if num_list[mid]<target:
            left = mid+1
        else:
            right = mid-1
    if num_list[left]!=target:
        return [-1,-1]
    result = [left]
    left, right = 0, len(num_list) -1
    while left <= right:
        mid = int((left + right) / 2)
        if num_list[mid] > target:
        	right = mid-1
        else:
        	left = mid + 1

    result.append(left-1)
    return result
print(finding_nearest_target([5,7,7,7,8,8,8,10],7))