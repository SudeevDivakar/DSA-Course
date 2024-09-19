class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    #write code here
    res = []
    
    if not root:
        return res
        
    stack = [root]
    
    while len(stack) > 0:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return res
    
# Time Complexity = O(n) - visit every node once and perform constant time operations
# Space Complexity = O(h) - where h is the height of the tree. In worst case, whenever we go down a level, we pop one node and add two nodes. This will result in the maximum space being used becoming O(h).