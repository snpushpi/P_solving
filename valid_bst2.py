'''
	Given a binary tree, determine if it is a valid binary search tree (BST).
	Assume a BST is defined as follows:
	The left subtree of a node contains only nodes with keys less than the node's key.
	The right subtree of a node contains only nodes with keys greater than the node's key.
	Both the left and right subtrees must also be binary search trees.
'''
class Node():
    def __init__(self,v):
        self.val = v
        self.left = None
        self.right = None
def max_val(node):
    if node.right== None and node.left== None:
        return node.val
    elif node.left == None:
        return max(node.val, max_val(node.right))
    elif node.right == None:
        return max(node.val, max_val(node.left))
    else:
        return max(max_val(node.left), node.val, max_val(node.right))
def min_val(node):
    if node.right== None and node.left== None:
        return node.val
    elif node.left == None:
        return min(node.val, min_val(node.right))
    elif node.right == None:
        return min(node.val, min_val(node.left))
    else:
        return min(min_val(node.left), node.val, min_val(node.right))
def isvalidbst(root):
    if root.left== None and root.right==None:
        return True
    elif root.left== None:
        return root.val<min_val(root.right)
    elif root.right== None:
        return max_val(root.left)<root.val
    else:
        return max_val(root.left)<root.val and root.val<min_val(root.right)