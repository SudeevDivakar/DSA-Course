def climbStairs(n):
    #write code here
    #n>=1
    if n <= 2:
        return n
        
    prev, curr = 1, 2
    
    for i in range(n - 2):
        next = prev + curr
        prev = curr
        curr = next
        
    return curr
        

# Time Complexity = O(n)
# Space Complexity = O(1)