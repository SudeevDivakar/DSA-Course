from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def dfs_in_order(self):
        #write code here
        res = []
        
        if not self.root:
            return res
            
        def helper(node):
            if node.left:
                helper(node.left)
            res.append(node.value)
            if node.right:
                helper(node.right)
                
        helper(self.root)
        
        return res

    def dfs_pre_order(self):
        #write code here
        res = []
        
        if not self.root:
            return res
        
        def helper(node):
            res.append(node.value)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
                
        helper(self.root)
        
        return res

    def dfs_post_order(self):
        #write code here
        res = []
        
        if not self.root:
            return res
        
        def helper(node):
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            res.append(node.value)
            
        helper(self.root)
        
        return res
    
# Time Complexity = O(n) since we visit every node once and do constant time operations.
# Space Complexity = O(n) since we are using an array to store the output. O(d) (depth of call stack) if we directly print output.