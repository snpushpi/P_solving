'''
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.
paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.
Also, there is no garden that has more than 3 paths coming into or leaving it.
Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.
Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.
 
Example 1:
Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Example 2:
Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:
Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
 
Note:
1 <= N <= 10000
0 <= paths.size <= 20000
No garden has 4 or more paths coming into or leaving it.
It is guaranteed an answer exists.
'''
def color(paths):
    neighbor_dict={}
    for elt in paths:
        if elt[0] in neighbor_dict:
            neighbor_dict[elt[0]].add(elt[1])
        else:
            neighbor_dict[elt[0]]=set()
            neighbor_dict[elt[0]].add(elt[1])
        if elt[1] in neighbor_dict:
            neighbor_dict[elt[1]].add(elt[0])
        else:
            neighbor_dict[elt[1]]=set()
            neighbor_dict[elt[1]].add(elt[0])
    color_dict = {e:0 for e in neighbor_dict}
    for elt in neighbor_dict:
        temp_color_set = set()
        for e in neighbor_dict[elt]:
            temp_color_set.add(color_dict[e])
        s = {1,2,3,4}
        rem_col = list(s-temp_color_set)[0]
        color_dict[elt]= rem_col
    result_list=[]
    l = len(color_dict)
    for i in range(l):
        result_list.append(color_dict[i+1])
    return result_list
print(color([[1,2],[2,3],[3,1]]))


