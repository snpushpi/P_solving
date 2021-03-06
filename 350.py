'''
	Given two arrays, write a function to compute their intersection.
	Example:
	Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
	Note:
	Each element in the result should appear as many times as it shows in both arrays.
	The result can be in any order.
	Follow up:
	What if the given array is already sorted? How would you optimize your algorithm?
	What if nums1's size is small compared to nums2's size? Which algorithm is better?
	What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''
def main(nums1,nums2):
    nums1.sort()
    nums2.sort()
    index1, index2 = 0,0
    result = []
    while index1<=len(nums1)-1 and index2<=len(nums2)-1:
        if nums1[index1]<nums2[index2]:
            index1+=1
        elif nums1[index1]>nums2[index2]:
            index2+=1
        else:
            index1+=1
            index2+=1
            result.append(nums1[index1])
    return result
print(main([1,2,2,1],[2,2]))
        