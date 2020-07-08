'''
	You are given an n x n 2D matrix representing an image.
	Rotate the image by 90 degrees (clockwise).
'''
def rotate(matrix):
    n = len(matrix)
    if n%2==0:
        m = int(n/2)
    else:
        m = int(n/2)+1
    for i in range(int(n/2)):
        for j in range(m):
            temp = matrix[i][j]
            matrix[i][j]=matrix[n-1-i][i]
            matrix[n-1-i][n-1-j]=matrix[n-1-i][j]
            matrix[j][n-1-i]=temp
            
    