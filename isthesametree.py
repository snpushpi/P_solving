'''
	Given two binary trees, write a function to check if they are the same or not.
	Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
	Example 1:
	Input:     1         1
	          / \       / \
	         2   3     2   3
	        [1,2,3],   [1,2,3]
	Output: true
'''
def isthesametree(tree1, tree2):
    if tree1== None and tree2== None:
        return True
    if tree1.left is not None and tree2.left is None:
        return False
    if tree1.left is None and tree2.left is not None:
        return False
    if tree1.right is not None and tree2.right is None:
        return False
    if tree1.right is None and tree2.right is not None:
        return False
    return tree1.val==tree2.val and isthesametree(tree1.left, tree2.left) and isthesametree(tree1.right, tree2.right)