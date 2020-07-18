'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
Note: A leaf is a node with no children.
Example:
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
'''
class Tree():
    def __init__(self,x):
        self.val=x
        self.left = None
        self.right = None
def sumNumber(root):
    def dfs(node, sum, result):
        if not root:
            return result
        sum = 10*sum+node.val
        if not root.left and not root.right:
            result+=sum
            return result
        return dfs(root.left, sum)+dfs(root.right, sum)
    return dfs(root, 0, 0)
    