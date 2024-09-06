class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseLinkedList(head):
    #write code here
    current = head
    prev = None
    while current != None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        
    return prev

# Time Complexity = O(n)
# Space Complexity = O(1)