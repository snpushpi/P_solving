'''
	Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
	Example:
	Input: [0,1,0,3,12]
	Output: [1,3,12,0,0]
	Note:
	You must do this in-place without making a copy of the array.
	Minimize the total number of operations.
'''
def main(num_list):
    l = len(num_list)
    marker = 0
    for i in range(l):
        if num_list[i]!=0:
            num_list[marker]=num_list[i]
            marker+=1
    for i in range(marker,l):
        num_list[i]=0
    return num_list
print(main([0,1,0,3,12]))
   