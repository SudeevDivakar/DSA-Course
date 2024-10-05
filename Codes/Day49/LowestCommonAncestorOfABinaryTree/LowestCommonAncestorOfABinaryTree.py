class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def lowestCommonAncestor(root, p, q):
    #p and q are nodes
    #write code here
    if not root:
        return None
        
    pval = p.val
    qval = q.val
    
    def helper(node):
        if not node:
            return None
            
        if node.val == pval or node.val == qval:
            return node
            
        left = helper(node.left)
        right = helper(node.right)
        
        if left and not right:
            return left
            
        if right and not left:
            return right
            
        if right and left:
            return node

    return helper(root)
