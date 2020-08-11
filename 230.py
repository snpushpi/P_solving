'''
	Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
	Note: 
	You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
	Example 1:
	Input: root = [3,1,4,null,2], k = 1
	Output: 1
'''

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def main(root):
    if not root:
        return 0
    stack = [root]
    count, curr = 0, root
    visited = []
    while stack:
        if curr.left:
            curr = curr.left
            stack.append(curr.left)
        else:
            node = stack.pop()
            count+=1
            if count==k:
                return node.val 
            else:
                if node.right:
                    stack.append(node.right)
                    curr = node.right
                    
    return float('-inf')
