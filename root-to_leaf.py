'''Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
	Note: A leaf is a node with no children.
	Example:
	Given the below binary tree and sum = 22,
	      5
	     / \
	    4   8
	   /   / \
	  11  13  4
	 /  \      \
	7    2      1
'''
class Tree():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def root_to_leaf(root,sum):
    if not root:
        return None
    if not root.left and not root.right and root.val==sum:
        return True 
    return root_to_leaf(root.left, sum- root.val) or root_to_leaf(root.right, sum-root.val)
    