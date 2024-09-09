# Better to use a linked list rather than an array because removal from the start of an array is an O(n) time complexity task.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, value):
        # write your code here
        new_node = Node(value)
        if self.size == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        
        self.size += 1
            

    def dequeue(self):
        # write your code here
        #return the value of the removed node
        if self.size == 0:
            return None
        
        elif self.size == 1:
            value = self.first.value
            self.first = None
            self.last = None
        
        else:
            first_node = self.first
            value = first_node.value
            self.first = first_node.next
            first_node.next = None
            
        self.size -= 1
        
        return value
            
'''Enqueue'''
# Time Complexity = O(1)
# Space Complexity = O(1)

'''Dequeue'''
# Time Complexity = O(1)
# Space Complexity = O(1)