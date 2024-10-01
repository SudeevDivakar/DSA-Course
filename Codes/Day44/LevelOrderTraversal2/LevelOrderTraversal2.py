class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def levelOrderBottom(root):
    #write code here 
    output = []
    if not root:
        return output
        
    queue = [[root]]
    while len(queue) > 0:
        nodes = queue.pop(0)
        temp_output = []
        temp_queue = []
        
        for node in nodes:
            temp_output.append(node.val)
            if node.left:
                temp_queue.append(node.left)
            if node.right:
                temp_queue.append(node.right)
                
        if len(temp_queue) > 0:
            queue.append(temp_queue)
        
        if len(temp_output) > 0:
            output.append(temp_output)
            
    output = list(reversed(output))
    
    return output
        
# Time Complexity = O(n)
# Space Complexity = O(w) where w -> max width of the binary tree