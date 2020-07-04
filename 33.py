'''
	Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
	(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
	You are given a target value to search. If found in the array return its index, otherwise return -1.
	You may assume no duplicate exists in the array.
	Your algorithm's runtime complexity must be in the order of O(log n).
'''
def search(num_list, target):
    left, right = 0, len(num_list)-1
    while left<=right:
        mid = int((left+right)/2)
        if num_list[mid]==target:
            return mid
        if num_list[left]<=num_list[mid]:
            if num_list[left]<=target and target<=num_list[mid]:
                right = mid -1
            else:
                left = mid + 1

        else:
            if num_list[mid]<=target and target<-num_list[right]:
                left = mid +1
            else:
                right = mid -1
    return -1
            
print(search([4,5,6,7,0,1,2],6))
