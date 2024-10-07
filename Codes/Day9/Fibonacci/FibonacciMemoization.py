ht = {}

def fibonacci(n):
    global ht
    #write code here
    
    if n <= 1:
        return n
        
    if (n - 1) not in ht:
        ht[(n - 1)] = fibonacci(n - 1)
    
    if (n - 2) not in ht:
        ht[(n - 2)] = fibonacci(n - 2)
        
    return ht[n - 1] + ht[n - 2]
    
# Time Complexity = O(n)
# Space Complextity = O(n) - Space used by hashtable