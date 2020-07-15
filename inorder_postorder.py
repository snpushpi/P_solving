'''
	Given inorder and postorder traversal of a tree, construct the binary tree.
	Note:
	You may assume that duplicates do not exist in the tree.
	For example, given
	inorder = [9,3,15,20,7]
	postorder = [9,15,7,20,3]
	Return the following binary tree:
	    3
	   / \
	  9  20
	    /  \
	   15   7
 '''
class TreeNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def buildTree(inorder, postorder):
    def recursive(inorder, postorder, start, end):
        if start>end:
            return None
        node = TreeNode(postorder[end])
    
        if start==end:
            return node
        search_index = 0
        for i in range(start, end+1):
            if inorder[i]==node.val:
                search_index = i
                break
        node.left = recursive(inorder, postorder, start, search_index-1)
        node.right = recursive(inorder, postorder, search_index+1, end)
        return node
    return recursive(inorder, postorder, 0, len(inorder)-1)
