class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def buildTree(inorder, postorder):
    #write code here
    def helper(pstart, pend, istart, iend):
        if pstart > pend or istart > iend:
            return None
            
        root = TreeNode(postorder[pend])
        
        mid = inorder.index(postorder[pend])
        left_size = mid - istart
        
        root.left = helper(pstart, pstart + left_size - 1, istart, mid - 1)
    
        root.right = helper(pstart + left_size, pend - 1, mid + 1, iend)
        
        return root
        
    return helper(0, len(postorder) - 1, 0, len(inorder))
    
