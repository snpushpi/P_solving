'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.
Input: root = [1,2,3,4], x = 4, y = 3
Output: false
'''
def adjacent(node,node1,node2):
    if not node:
        return False
    value = False
    if node.left and node.right:
        if (node.left.val==node1.val and node.right.val==node2.val) or (node.left.val==node2.val and node.right.val==node1.val):
            value = True
    return value or adjacent(node.left,node1,node2) or adjacent(node.right,node1,node2)

def level(root,node,level):
    if not root:
        return 0
    if node.val==root.val:
        return level 
    left_level = level(node.left,node,level+1)
    if left_level!=0:
        return left_level
    return level(root.right,node,level+1)

def is_cousin(root,node1,node2):
    if level(root,node1,0)==level(root,node2,0) and not adjacent(root,node1,node2):
        return True
    return False

    