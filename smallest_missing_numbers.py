'''
	Given an unsorted integer array, find the smallest missing positive integer.
	Example 1:
	Input: [1,2,0]
	Output: 3
	Example 2:
	Input: [3,4,-1,1]
	Output: 2
	Example 3:
	Input: [7,8,9,11,12]
	Output: 1
'''

def modifier(nums):
    index_i=0
    for index_j in range(len(nums)):
        if nums[index_j] <= 0:
            nums[index_i], nums[index_j] = nums[index_j], nums[index_i]
            index_i += 1
    check_set = set(nums[index_i:])
    for i in range(1,len(check_set)):
        if i not in check_set:
            return i

print(modifier([-2,-3,1,2,-3,3,4,-9]))