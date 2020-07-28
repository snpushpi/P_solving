'''
Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.
(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)
Example 1:
	    8
	  /   
	3	   10
  /	  \      
1	   6	  14
	  /  \    /
	4	  7	 13
Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
 
Note:
The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
'''
class TreeNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def maxAncestorDiff(tree_node):
    def internal(node, res):
        if not tree_node:
            return 2147483648, -2147483648, res
        if not node.left and not node.right:
            return node.val, node.val, res
        left_min, left_max, res1 = internal(node.left, res)
        right_min, right_max, res2 = internal(node.right, res)
        min_val = min(left_min, right_min)
        max_val = max(left_max, right_max)
        res = max(abs(node.val-max_val), abs(node.val-min_val), res1, res2)
        own_min = min(node.val, min_val)
        own_max = max(node.val, max_val)
        return own_min, own_max, res
    x1, x2, res = internal(tree_node,-2147483648)
    return res 