'''
	Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
	Example 1:
	Input: [1,3,4,2,2]
	Output: 2
	Example 2:
	Input: [3,1,3,4,2]
	Output: 3
'''
def main(num_list):
    sum=0
    for num in num_list:
        sum+=num
    l = len(num_list)
    total_sum = (l*(l-1))//2
    return sum-total_sum
print(main([3,1,3,4,2]))
