'''
	Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
	Integers in each row are sorted in ascending from left to right.
	Integers in each column are sorted in ascending from top to bottom.
	Consider the following matrix:
	[
	  [1,   4,  7, 11, 15],
	  [2,   5,  8, 12, 19],
	  [3,   6,  9, 16, 22],
	  [10, 13, 14, 17, 24],
	  [18, 21, 23, 26, 30]
	]
	Example 1:
	Input: matrix, target = 5
	Output: true
'''
def main(matrix, target):
    left, right = 0, len(matrix[0])-1
    if not matrix:
        return False
    while left<=right:
        if matrix[left][right]==target:
            return True
        elif matrix[left][right]<target:
            left+=1
        elif matrix[left][right]>target:
            right-=1
    return False



