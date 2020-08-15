'''
Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.
Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def smalleststring(root,A):
    result = '~'
    def dfs(node,A):
        if node:
            A.append(chr(node.val+ord('a')))
            if not node.left and not node.right:
                result = min(result,"".join(reversed(A)))
            dfs(node.left,A)
            dfs(node.right,A)
            A.pop()
    dfs(root,[])
    return result