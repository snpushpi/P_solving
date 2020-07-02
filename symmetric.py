"""
STATEMENT
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
CLARIFICATIONS
- Can we assume that the node values have a well-defined equals (== in python, say) operator? Yes.
EXAMPLES
[1,2,2,3,4,4,3] -> True
[1,2,2,null,3,null,3] -> False
"""
def isSymmetric(root):
    if root is None:
        return True
    if isMirror(root.left, root.right):
        return True
    else:
        return False
def isMirror(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if (tree1.val==tree2.val):
        return (isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left))
    return False