class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

def linkNodes(node1,node2):
    node1.next = node2
    node2.prev = node1

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove(self, node):
        # write code here
        if self.head == self.tail == node:
            self.head = None
            self.tail = None
            
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None
            node.next = None
        
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
            node.prev = None

        elif node.prev and node.next:
            linkNodes(node.prev, node.next)
            node.prev = None
            node.next = None

    
    def insertB(self, nodePosition, nodeInsert):
        # Write your code here
        # remove node from linked list if it is already present
        
        # nodeInsert is already present before nodePosition
        if nodePosition.prev == nodeInsert:
            return
        
        # remove node from linked list
        self.remove(nodeInsert)

        # insert the node at head
        if nodePosition == self.head:
            nodeInsert.next = nodePosition
            nodeInsert.prev = None
            nodePosition.prev = nodeInsert
            self.head = nodeInsert
        # insert the node in between
        else:
            linkNodes(nodePosition.prev, nodeInsert)
            linkNodes(nodeInsert, nodePosition)
        
