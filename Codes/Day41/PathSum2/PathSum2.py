class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def pathSum(root, targetSum):
    #write code here
    res = []
    
    if not root:
        return res
        
    elements = []
    
    def helper(node):
        elements.append(node.val)
        if not node.left and not node.right and sum(elements) == targetSum:
            res.append(list(elements))
            
        if node.left:
            helper(node.left)
            
        if node.right:
            helper(node.right)
        
        elements.pop()
        
    helper(root)    
        
    return res
     

# Time Complexity = O(n * h)
# Space Complexity = O(h)