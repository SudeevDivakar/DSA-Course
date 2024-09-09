class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, val):
        #write code here
        self.inStack.append(val)

    def pop(self):
        #write code here
        if len(self.outStack) == 0 and len(self.inStack) == 0:
            return None
            
        elif len(self.outStack) == 0 and len(self.inStack) > 0:
            while len(self.inStack) != 0:
                self.outStack.append(self.inStack.pop())
        
            
        return self.outStack.pop()

    def peek(self):
        #write code here
        if len(self.outStack) == 0 and len(self.inStack) == 0:
            return None
        
        elif len(self.outStack) == 0 and len(self.inStack) > 0:
            while len(self.inStack) != 0:
                self.outStack.append(self.inStack.pop())
        
        return self.outStack[-1]
        
    def empty(self):
        # write code here
        if len(self.inStack) == 0 and len(self.outStack) == 0:
            return True
        else:
            return False
        
'''Time Complexity Analysis'''
# Empty = O(1)
# Peek = O(1)  (amortised)
# Pop = O(1)  (amortised) (Dequeue)
# Push = O(1)   (Enqueue)
# Overall Time Complexity = O(n)

'''Space Complexity Analysis'''
# Overall Space Complexity = O(n)