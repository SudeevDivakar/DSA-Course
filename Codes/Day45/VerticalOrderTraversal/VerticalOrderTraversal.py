class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, defaultdict

def verticalTraversal(root):
    #write code here
    output = []
    if not root:
        return output
        
    ht = {}
    
    min_y = float('inf')
    max_y = -float('inf')
    
    def helper(node, x, y):
        nonlocal min_y, max_y
        if not node:
            return
        
        if (x, y) not in ht:
            ht[(x, y)] = [node.val]
        else:
            ht[(x, y)].append(node.val)
            
        if y < min_y:
            min_y = y
            
        if y > max_y:
            max_y = y
            
        helper(node.left, x + 1, y - 1)
        helper(node.right, x + 1, y + 1)
        
    helper(root, 0, 0)
    
    for i in ht:
        ht[i] = list(sorted(ht[i]))
    
    while min_y <= max_y:
        temp_output = []
        for i in list(sorted(list(ht.keys()))):
            if i[1] == min_y:
                temp_output.extend(ht[i])
                
        min_y += 1
                
        output.append(temp_output)
    
    return output