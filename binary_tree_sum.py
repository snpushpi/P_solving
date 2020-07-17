'''
	Given a non-empty binary tree, find the maximum path sum.
	For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
	Example 1:
	Input: [1,2,3]
	       1
	      / \
	     2   3
	Output: 6
	Example 2:
	Input: [-10,9,20,null,null,15,7]
	   -10
	   / \
	  9  20
	    /  \
	   15   7
	Output: 42
'''
def bin_tree_sum(node):
    result = float('-inf')
    def dfs(node):
        if not node:
            return 0
        l = bin_tree_sum(node.left)
        r = bin_tree_sum(node.right)
        max_one_end = max(max(l,r)+node.val, node.val)
        max_path = max(max_one_end, l+r+node.val)
        result = max(result, max_path)
        return max_one_end
    dfs(node)
    return result

