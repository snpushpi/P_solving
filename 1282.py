'''
There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.
You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution. 
 
Example 1:
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
Example 2:
Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
'''
def main(groupsizes):
    l = len(groupsizes)
    group_dict={}
    for i in range(l):
        if groupsizes[i] in group_dict:
            group_dict[groupsizes[i]].append(i)
        else:
            group_dict[groupsizes[i]]=[]
            group_dict[groupsizes[i]].append(i)
    print(group_dict)
    result=[]
    for elt in group_dict:
        list1 = group_dict[elt]
        l = len(list1)
        for i in range(0,l,elt):
            chunk = list1[i:i+elt]
            result.append(chunk)
    return result
print(main([2,1,3,3,3,2]))
