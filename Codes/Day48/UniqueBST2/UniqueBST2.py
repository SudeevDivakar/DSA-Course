class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def generateTrees(n):
    #write code here
    if n == 0:
        return []
        
    dp = {}
    
    def helper(left, right):
        if left > right:
            return [None]
            
        if (left, right) in dp:
            return dp[(left,right)]
            
        res = []
        
        for val in range(left, right + 1):
            for leftTree in helper(left, val - 1):
                for rightTree in helper(val + 1, right):
                    root = TreeNode(val, leftTree, rightTree)
                    res.append(root)
                    
        dp[(left, right)] = res
        return dp[(left, right)]
    
    return helper(1, n)