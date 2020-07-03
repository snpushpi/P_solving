'''
	Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
	If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
	The replacement must be in-place and use only constant extra memory.
	Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
	1,2,3 → 1,3,2
	3,2,1 → 1,2,3
	1,1,5 → 1,5,1
'''
def next_permutation(num_list):
    l = len(num_list)
    inc_index = 0
    strictly_decreasing = True
    strictly_increasing = True
    for i in range(1,l-1):
        if num_list[i-1]<=num_list[i] and num_list[i]>=num_list[i+1]:
            inc_index=i
    for i in range(l-1):
        if num_list[i]<num_list[i+1]:
            strictly_decreasing = False
        if num_list[i]>num_list[i+1]:
            strictly_increasing = False
    print(strictly_decreasing, strictly_increasing)
    if not strictly_decreasing and not strictly_increasing:
        swap = num_list[inc_index]
        num_list[inc_index]=num_list[inc_index-1]
        num_list[inc_index-1]=swap
    elif strictly_decreasing:
        for i in range(int(l/2)):
            swap = num_list[i]
            num_list[i]=num_list[l-1-i]
            num_list[l-1-i]=swap
    else:
        print('hi')
        swap = num_list[l-1]
        num_list[l-1]=num_list[l-2]
        num_list[l-2]=swap

    return num_list
print(next_permutation([1,2,3]))