class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    #write code here
    res = []
    
    if not root:
        return res
        
    curr = root
    stack = []
    while curr or len(stack) > 0:
        while curr:
            stack.append(curr)
            curr = curr.left
        
        node = stack.pop()
        res.append(node.val)
        if node.right:
            curr = node.right
    
    return res

# Time Complexity = O(n)
# Space Complexity = O(n) - worst case would be a completely skewed binary tree and we would have to add all the values to the stack.