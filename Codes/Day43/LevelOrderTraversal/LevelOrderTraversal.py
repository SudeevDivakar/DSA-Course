from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, array):
        #write code here
        #return self once you are done
        if len(array) == 0 or array[0] == None:
            return None
        
        self.root = Node(array[0])
        
        i = 1
        # Check if only one element in array
        if i == len(array):
            return self
        
        queue = [self.root]
        
        while len(queue) > 0:
            node = queue.pop(0)
            
            # Add to left if nothing there and element in array is not None
            if not node.left:
                if array[i] != None:
                    node.left = Node(array[i])
                i += 1
                if i == len(array):
                    return self
                
            # Append to queue is something is there on left side
            if node.left:
                queue.append(node.left)
                
            # Add to right if nothing is there and element in array is not None
            if not node.right:
                if array[i] != None:
                    node.right = Node(array[i])
                i += 1
                if i == len(array):
                    return self

            # Append to queue if something is there in right side
            if node.right:
                queue.append(node.right)
                    
                    
def level_order_traversal(root):
    if root is None:  
        return []

    output = []
    #write your code here
    queue = [[root]]
    
    while len(queue) > 0:
        nodes = queue.pop(0)
        temp_output = []  # To store outputs of each level
        temp_queue = []
        for node in nodes:
            temp_output.append(node.value)
            if node.left:
                temp_queue.append(node.left)
            if node.right:
                temp_queue.append(node.right)
        
        if len(temp_output) > 0:
            output.append(temp_output)
        if len(temp_queue) > 0:
            queue.append(temp_queue)
        
    return output

#For you to test by yourself
# Create a binary tree and insert elements
tree = BinaryTree()
tree.insert([7, 11, 1, None, 7, 2, 8, None, None, None, 3, None, None, 5, None])


# Time Complexity = O(n)
# Space Complexity = O(w) where w -> max width of the binary tree