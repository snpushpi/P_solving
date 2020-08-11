'''
	Invert a binary tree.
	Example:
	Input:
	     4
	   /   
	  2     7
	 / \   / 
	1   3 6   9
	Output:
	     4
	   /   
	  7     2
	 / \   / 
	9   6 3   1
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def main(root):
    if not root:
        return None
    lefttree = main(root.right)
    righttree = main(root.left)
    root.left = righttree
    root.right = lefttree
    return root


