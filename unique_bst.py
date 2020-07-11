class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def generateTrees(n):
    if n==0:
        return []
    def generate(start, end):
        result = []
        if start>end:
            result.append(None)
            return result
        for index in range(start, end+1):
            left_tree = generate(start, index-1)
            right_tree = generate(index+1, end)
            for l in left_tree:
                for r in right_tree:
                    current = TreeNode(index)
                    current.left = l
                    current.right = r
                    result.append(current)
        return result
    return generate(1,n)
print(generateTrees(4))