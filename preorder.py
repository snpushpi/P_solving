'''
Return the root node of a binary search tree that matches the given preorder traversal.
(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def generate_tree(preorder_list):
    if len(preorder_list)==0:
        return None
    node = TreeNode(preorder_list[0])
    for i in range(1, len(preorder_list)):
        if preorder_list[i]>preorder_list[0]:
            node.left = generate_tree(preorder_list[:i])
            node.right = generate_tree(preorder_list[i:])
            return node
    node.left = generate_tree(preorder_list[1:])
    node.right = generate_tree([])
    return node
