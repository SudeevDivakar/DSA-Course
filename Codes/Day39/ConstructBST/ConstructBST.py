class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        #write your code here
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            node = self.root
            while True:
                if value >= node.value:
                    if node.right:
                        node = node.right
                    else:
                        node.right = new_node
                        break
                elif value < node.value:
                    if node.left:
                        node = node.left
                    else:
                        node.left = new_node
                        break

    def find(self, value):
        #write your code here
        node = self.root
        while node != None:
            if node.value == value:
                return node
            elif value > node.value:
                node = node.right
            elif value < node.value:
                node = node.left
        
        return False

    def remove(self, value, current=None, parent=None):
        #write your code here
        if self.root == None:
            return
            
        if current == None:
            current = self.root
            
        while current:
            if value < current.value:
                parent = current
                current = current.left
                
            elif value > current.value:
                parent = current
                current = current.right
                
            else:
                if current.right and current.left:
                    current.value = self.get_min(current.right)
                    self.remove(current.value, current.right, current)
                    
                elif parent == None:
                    if current.left:
                        left_node = current.left
                        current.left = None
                        current.value = None
                        self.root = left_node
                    elif current.right:
                        right_node = current.right
                        current.right = None
                        current.value = None
                        self.root = right_node
                    else:
                        self.root = None
                    
                elif parent.left == current:
                    parent.left = current.left if current.left else current.right
                    
                elif parent.right == current:
                    parent.right = current.left if current.left else current.right
                    
                break
        
        return self

    def get_min(self, node):
        while node.left:
            node = node.left
        return node.value
    
# Time Complexity = O(log n) for insertion, removal and deletion best and O(n) for insertion, deletion and removal worst.
# Space Complexity = O(1) for iterative approach. O(log n) for recursive approach best and O(n) for recursive approach worst.