class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def checkLoop(head):
    #write your code here
    current = head
    hashtable = {}
    if not head:
        return None
    
    while current.next != None:
        if current.next in hashtable:
            return current.next
            
        else:
            hashtable[current] = True
            current = current.next
    
    return None

# Time Complexity = O(n)
# Space Complexity = O(n) 