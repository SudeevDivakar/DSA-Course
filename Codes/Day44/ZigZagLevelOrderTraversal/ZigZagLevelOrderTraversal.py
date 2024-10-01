from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    #write code here
    output = []
    
    if not root:
        return output
        
    queue = [[root]]
    
    while len(queue) > 0:
        nodes = queue.pop()
        temp_output = []
        temp_queue = []
        
        for node in nodes:
            temp_output.append(node.val)
            if node.left:
                temp_queue.append(node.left)
            if node.right:
                temp_queue.append(node.right)
                
        if len(temp_output) > 0:
            output.append(temp_output)
            
        if len(temp_queue) > 0:
            queue.append(temp_queue)
            
    
    for i in range(len(output)):
        if i % 2 != 0:
            output[i] = list(reversed(output[i]))
            
    return output