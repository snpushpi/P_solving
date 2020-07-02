"""
STATEMENT
Given a binary tree, determine if it is a valid binary search tree (BST).
CLARIFICATIONS
- For any root, the max of the left subtree is smaller than the current value and
  the min of the right subtree is bigger than the current value. Yes, and both the
  left and right subtrees are also BST.
- I am assuming the tree nodes are custom data structure? Yes, define it.
- Is an empty tree BST or a single element tree BST? Yes.
EXAMPLES
  1
2
  3
-> True
"""
class Treenode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def min_value(tree):
    if tree is None:
        return -1
    if tree.left is None and tree.right is None:
        return tree.val
    if tree.left is None:
        return tree.val
    if tree.right is None:
        return min_value(tree.left)
    return min_value(tree.left)
def max_value(tree):
    if tree is None:
        return -1
    if tree.left is None and tree.right is None:
        return tree.val
    if tree.left is None:
        return max_value(tree.right)
    if tree.right is None:
        return tree.val 
    return max_value(tree.right)

def isvalid(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is None:
        return isvalid(root.right) and (root.val < min_value(root.right))
    if root.right is None:
        return isvalid(root.left) and (root.val > max_value(root.left))
    return isvalid(root.left) and isvalid(root.right) and max_value(root.left)<root.val and root.val<min_value(root.right)