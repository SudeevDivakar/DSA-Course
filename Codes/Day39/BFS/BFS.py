from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def bread_first(self):
        #write code here
        res = []
        
        if not self.root:
            return res
            
        queue = [self.root]
        
        while len(queue) > 0:
            node = queue.pop(0)
            res.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return res
        
        
# Time Complexity = O(n) since we visit every node once and do constant time operations.
# Space Complexity = O(n) since we are using an array to store the output. O(w) (max width of BST) as this would be the space required for the queue.