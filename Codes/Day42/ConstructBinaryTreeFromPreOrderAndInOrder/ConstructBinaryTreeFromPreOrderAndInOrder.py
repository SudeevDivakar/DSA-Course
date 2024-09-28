class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    #write code here
    def helper(pstart, pend, istart, iend):
        if pstart > pend or istart > iend:
            return None
            
        root = TreeNode(preorder[pstart])
        
        mid = inorder.index(preorder[pstart])
        left_index = mid - istart
        
        root.left = helper(pstart + 1, pstart + left_index, istart, mid - 1)
        root.right = helper(pstart + left_index + 1, pend, mid + 1, iend)
        
        return root
    
    return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
    