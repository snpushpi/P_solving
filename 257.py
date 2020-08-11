'''
	Given a binary tree, return all root-to-leaf paths.
	Note: A leaf is a node with no children.
	Example:
	Input:
	   1
	 /   
	2     3
	 
	  5
	Output: ["1->2->5", "1->3"]
	Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''
def main(root):
    paths = []
    def dfs(node,curr):
        if node.left is None and node.right is None:
            paths.append(curr+str(node.val))
        if node.left:
            dfs(node.left,curr+'->'+str(node.val))
        elif node.right:
            dfs(node.right,curr+'->'+str(node.val))
    dfs(root,'')
    return paths 

