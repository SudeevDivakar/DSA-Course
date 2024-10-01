def rightView(root):
    if root is None: 
        return []
    right = []
    #write your code here
    queue = [[root]]
    
    while len(queue) > 0:
        nodes = queue.pop()
        
        right.append(nodes[-1].value)
        
        temp_queue = []
        
        for node in nodes:
            if node.left:
                temp_queue.append(node.left)
                
            if node.right:
                temp_queue.append(node.right)
        
        if len(temp_queue) > 0:
            queue.append(temp_queue)
        
    return right

def leftView(root):
    if root is None: 
        return []
    left = []
    #write your code here
    
    queue = [[root]]
    
    while len(queue) > 0:
        nodes = queue.pop()
        left.append(nodes[0].value)
        
        temp_queue = []
        for node in nodes:
            if node.left:
                temp_queue.append(node.left)
            if node.right:
                temp_queue.append(node.right)
        
        if len(temp_queue) > 0:
            queue.append(temp_queue)
            
    return left

# Time Complexity = O(n)
# Space Complexity = O(w) where w -> max width of the binary tree