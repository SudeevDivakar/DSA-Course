def fibonacci(n):
    if n <= 1:
        return n
        
    dp = [0] * (n + 1)
    
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]
    

# Time Complexity = O(n)
# Space Complexity = O(n) - Space taken up by the DP list