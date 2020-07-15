'''
    Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
    For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its zigzag level order traversal as:
    [
      [3],
      [20,9],
      [15,7]
    ]
'''
class Tree():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def zigzag(root_node):
    level = [root_node]
    result = []
    while level:
        add_list =[]
        node_list =[]
        for elt in level:
            if elt.left is not None:
                add_list.append(elt.left.val)
                node_list.append(elt.left)
            if elt.right is not None:
                add_list.append(elt.right.val)
                node_list.append(elt.right)
        result.append(add_list)
        level = node_list
    return result

