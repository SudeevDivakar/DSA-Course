def fibonacci(n):
    #write code here
    if n == 0:
        return 0
    
    if n == 1:
        return 1
        
    return fibonacci(n - 1) + fibonacci(n - 2)


# Time Complexity = O(2 ^ n)
# Space Complexity = O(n) - Space used by the recursive call stack