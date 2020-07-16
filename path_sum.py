'''
	Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
	Note: A leaf is a node with no children.
	Example:
	Given the below binary tree and sum = 22,
	      5
	     / 
	    4   8
	   /   / 
	  11  13  4
	 /  \    / 
	7    2  5   1
	Return:
	[
	   [5,4,11,2],
	   [5,8,4,5]
	]
'''
def all_paths(node, sum):
    result =[]
    def path_creator(node, curr_sum, path, result):
        curr_sum+=node.val
        if not node.left and not node.right and curr_sum==sum:
            result.append(path+[node.val])
            return 
        if node.left:
            path_creator(node.left, curr_sum+node.val, path+[node.val], result)
        if node.right:
            path_creator(node.right, curr_sum+node.val, path+[node.val], result)
        
    path_creator(node, 0, [], result)
    return result
