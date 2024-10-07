def fibonacci(n):
    if n <= 1:
        return n
        
    prev = 0
    curr = 1

    for i in range(n - 1):
        next = prev + curr
        prev = curr
        curr = next
        
    return curr

# Time Complexity = O(n)
# Space Complexity = O(1)