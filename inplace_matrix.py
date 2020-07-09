'''
	Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
	Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
	Example 1:
	Given nums = [1,1,1,2,2,3],
	Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
	It doesn't matter what you leave beyond the returned length.
'''
def removeDuplicates(nums):
    if len(nums)<=2:
        return len(nums)
    prev, curr = 1, 2
    while curr<len(num):
        if nums[prev]==nums[curr] and nums[prev-1]==nums[curr]:
            curr+=1
        else:
            prev+=1
            nums[prev]=nums[curr]
            curr+=1
    return prev+=1
