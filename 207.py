'''
	There are a total of n courses you have to take, labeled from 0 to n-1.
	Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
	Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
	Example 1:
	Input: 2, [[1,0]] 
	Output: true
	Explanation: There are a total of 2 courses to take. 
	             To take course 1 you should have finished course 0. So it is possible.
'''
def iscyclic(graph_dict,elt,visited,recstack):
    visited[elt]=True
    recstack[elt]=True
    for neighbor in graph_dict[elt]:
        if iscyclic(graph_dict,neighbor,visited,recstack)==True:
            return True
        elif recstack[neighbor]==True:
            return True
    recstack[elt]=False
    return False
def main(course_list):
    graph_dict = {}
    for elt in course_list:
        if elt[0] not in graph_dict:
            graph_dict[elt[0]]=[elt[1]]
        else:
            graph_dict[elt[0]].append(elt[1])
    #now will do dfs to find cycle
    vertices = list(graph_dict.keys())
    visited = {e:False for e in vertices}
    recstack = {e:False for e in vertices}
    for elt in vertices:
        if visited[elt]==False:
            if iscyclic(graph_dict,elt,visited,recstack)==True:
                return False
    return True
print(main([[1,0],[0,1]]))
