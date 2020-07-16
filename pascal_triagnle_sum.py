'''
    Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
    For example, given the following triangle
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
'''
def pascal_tri_sum(list_of_lists):
    result_tri =[]
    l = len(list_of_lists)
    for row in range(l):
        result_tri.append([0 for i in range(row+1)])
        result_tri[0][0]=list_of_lists[0][0]
    for i in range(1,l):
        for j in range(len(list_of_lists[i])):
            if j==0:
                result_tri[i][j]=list_of_lists[i][j]+result_tri[i-1][j]
            elif j==len(list_of_lists[i])-1:
                result_tri[i][j]=list_of_lists[i][j]+result_tri[i-1][j-1]
            else:
                result_tri[i][j]=list_of_lists[i][j]+ min(result_tri[i-1][j-1], result_tri[i-1][j])
    mini = float('inf')
    for elt in result_tri[l-1]:
        if mini>elt:
            mini=elt
    return mini

print(pascal_tri_sum([[2],[3,4],[6,5,7],[4,1,8,3]]))

