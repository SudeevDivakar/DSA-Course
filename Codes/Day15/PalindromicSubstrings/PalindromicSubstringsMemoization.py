def countSubstrings(s):
    #write code here
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    def helper(i, j):
        if i == j:
            dp[i][j] = True
            return True
            
        if dp[i][j] != 0:
            return dp[i][j]

        helper(i + 1, j)
        helper(i, j - 1)
            
        if s[i] == s[j] and (j == i + 1 or helper(i + 1, j - 1)):
            dp[i][j] = True
        
    helper(0, n - 1)
    
    count = 0
    
    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if dp[i][j]:
                count += 1
                
    return count

# Time Complexity = O(n ^ 2)
# Space Complexity = O(n ^ 2)