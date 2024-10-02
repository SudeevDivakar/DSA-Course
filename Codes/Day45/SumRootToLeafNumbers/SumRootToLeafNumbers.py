class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def sumNumbers(root):
    #write code here
    if not root:
        return 0
    
    output = 0
        
    def helper(node, num):
        nonlocal output
        num = (num * 10) + node.val
        if not node.left and not node.right:
            output += num
        
        else:
            if node.left:
                helper(node.left, num)
            if node.right:
                helper(node.right, num)
        
    helper(root, 0)
    
    return output