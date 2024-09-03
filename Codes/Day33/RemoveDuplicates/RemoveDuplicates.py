class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def removeDupes(head):
    #write code here
    current = head
    
    while current != None:
        if current.next and current.next.val == current.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head

# Time Complexity = O(n)
# Space Complexity = O(1)