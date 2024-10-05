class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    # Start from the root node
    #p and q are 2 nodes
    #write code here
    if not root:
        return None
    
    pval = p.val
    qval = q.val
    
    while root:
        if root.val > pval and root.val > qval:
            root = root.left
            
        elif root.val < pval and root.val < qval:
            root = root.right
            
        else:
            return root

