"""
STATEMENT
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
CLARIFICATIONS
- Do we print all 'None' values that a level may have? Yes.
EXAMPLES
[3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]
"""
def levelOrder(root):
    to_return = []
    if not root:
        return to_return
    level = [root]
    while level:
        next_level, current_level_val = [], []
        for node in level:
            next_level.append(node.left)
            next_level.append(node.right)
            current_level_val.append(node.val)
        level = next_level
        if current_level_val:
            to_return.append(current_level_val)
    return to_return
