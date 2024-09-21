class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def postorderTraversal(root):
    #write code here
    res = []
    
    if not root:
        return res
        
    stack = [root]
    visited = [False]
    
    while len(stack) > 0:
        curr = stack.pop()
        v = visited.pop()
        
        if v:
            res.append(curr.val)
            
        else:
            stack.append(curr)
            visited.append(True)
            if curr.right:
                stack.append(curr.right)
                visited.append(False)
            if curr.left:
                stack.append(curr.left)
                visited.append(False)
                    
    return res
        

# Time Complexity = O(n)
# Space Complexity = O(h) where h -> height of tree. Best Case = O(log n), Worst Case = O(n)
