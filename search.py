'''
	Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
	(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
	You are given a target value to search. If found in the array return true, otherwise return false.
	Example 1:
	Input: nums = [2,5,6,0,0,1,2], target = 0
	Output: true
	Example 2:
	Input: nums = [2,5,6,0,0,1,2], target = 3
	Output: false
'''
def search(nums, target):
    left, right = 0, len(nums)-1
    mid = int((left+right)/2)
    wwhile left<=right:
        if nums[mid]==target:
            return mid
        elif nums[left]<nums[mid]:
            if nums[left]<target<nums[mid]:
                right=mid-1
            else:
                left=mid+1

        elif nums[mid]<nums[left]:
            if nums[mid]<target<=nums[right]:
                left = mid+1
            else:
                right=mid-1
        else:
            left+=1