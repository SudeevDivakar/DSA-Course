def tribonacci(n):
    #write code here
    if n <= 1:
        return n
    
    if n == 2:
        return 1
    
    a = 0
    b = 1
    c = 1
    
    for i in range(n - 2):
        next = a + b + c
        a = b
        b = c
        c = next
        
    return c

# Time Complexity = O(n)
# Space Complexity = O(1)