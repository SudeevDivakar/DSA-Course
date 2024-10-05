class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        if children is None:
            self.children = []
        else:
            self.children = children
            
from collections import deque

def levelOrder(root):
    #write code here
    if not root:
        return []
        
    res = [[root.val]]
    
    queue = [root.children]
    
    while len(queue) > 0:
        nodes = queue.pop(0)
        temp_res = []
        temp_queue = []
        
        for node in nodes:
            temp_queue.extend(node.children)
            temp_res.append(node.val)
        
        if len(temp_queue) > 0:
            queue.append(temp_queue)
        
        if len(temp_res) > 0:
            res.append(temp_res)
            
    return res