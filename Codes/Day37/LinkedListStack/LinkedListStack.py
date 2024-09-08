# We push and pop element from beginning of linked list as removal from end of a singly linked list is an O(n) task
# If we use a doubly linked list, we can push and pop elements from either the beginning or end as both are constant time tasks.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def addAtBeginning(self, value):
        # write your code here
        if self.size == 0:
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
        else:
            new_node = Node(value)
            new_node.next = self.first
            self.first = new_node
            
        self.size += 1
        
        return self

    def removeFromBeginning(self):
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
      
''' Pushing Elements: '''
# Time Complexity = O(1)
# Space Complexity = O(1)

'''Popping Elements'''
# Time Complexity = O(1)
# Space Complexity = O(1) 