'''
	Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
		Note: The solution set must not contain duplicate subsets.
		Example:
		Input: [1,2,2]
		Output:
		[
		  [2],
		  [1],
		  [1,2,2],
		  [2,2],
		  [1,2],
		  []
		]
'''
def subsetwithdup(nums):
    result = [[]]
    for num in nums:
        l = len(result)
        for index in range(l):
            new_list = result[index]+[num]
            new_list.sort()
            result.append(new_list)
    unique = set(tuple(val) for val in result)
    return list(list(val) for val in unique)
print(subsetwithdup([1,2,2]))