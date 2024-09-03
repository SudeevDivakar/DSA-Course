class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        #write code here
        if not self.head:
            return -1
            
        elif index < 0 or index >= self.size:
            return -1
        
        else:
            current = self.head
            counter = 0
            
            while counter < index:
                current = current.next
                counter += 1
                
            return current

    def addAtHead(self, value):
        #write code here
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
            
        else:
            new_node.next = self.head
            self.head = new_node
            
        self.size += 1
        
        return self

        
    def addAtTail(self, value):
        #write code here
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
        
        return self
        

    def addAtIndex(self, index, value):
        #write code here
        if index < 0 or index > self.size:
            return 'invalid index'
        
        elif index == 0:
            self.addAtHead(value)
            
        elif index == self.size:
            self.addAtTail(value)
            
        else:
            new_node = Node(value)
            
            current = self.head
            counter = 0
            
            while counter < index - 1:
                current = current.next
                counter += 1
        
            new_node.next = current.next
            current.next = new_node
        
            self.size += 1
        
        return self
        
                
    def deleteAtIndex(self, index):
        #write code here
        if index < 0 or index >= self.size:
            return
        
        elif self.size == 1:
            deleted_node = self.head
            self.head = None
            self.tail = None
        
        elif index == 0:
            deleted_node = self.head
            self.head = deleted_node.next
            deleted_node.next = None
            
        elif index == self.size - 1:
            current = self.head
            counter = 0
            
            while counter < index - 1:
                current = current.next
                counter += 1
                
            deleted_node = current.next
            current.next = None
            self.tail = current

        else:
            current = self.head
            counter = 0
            
            while counter < index - 1:
                current = current.next
                counter += 1
            
            deleted_node = current.next
            current.next = deleted_node.next
            deleted_node.next = None
                    
        self.size -= 1
            
        return deleted_node