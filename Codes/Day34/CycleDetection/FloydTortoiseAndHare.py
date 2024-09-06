class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def checkLoop(head):
    #write your code here
    hare = head
    tortoise = head
    
    while hare != None:
        if hare.next == None:
            return None
        
        hare = hare.next.next
        tortoise = tortoise.next

        if hare == tortoise:
            start = head
            end = tortoise
            
            while start != end:
                start = start.next
                end = end.next
            
            return start
            
    return None

# Time Complexity = O(n)
# Space Complexity = O(1)