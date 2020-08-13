  
'''
	Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
	Formally the function should:
	Return true if there exists i, j, k 
	such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
	Your algorithm should run in O(n) time complexity and O(1) space complexity.
	Examples:
	Given [1, 2, 3, 4, 5],
	return true.
	Given [5, 4, 3, 2, 1],
	return false.
'''
def main(nums):
    first, second = float('inf'), float('inf')
    for val in nums:
        if val<=first:
            first=val 
        if val<=second:
            second=val
        else:
            return True
    return False
print(main([5,4,3,2,1]))        