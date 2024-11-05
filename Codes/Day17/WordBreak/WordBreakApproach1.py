def wordBreak(s, wordDict):
    #Write code here
    n = len(s)
    
    dp = [[False] * n for _ in range(n)]
    
    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            
            if s[i: j + 1] in wordDict:
                dp[i][j] = True
            
            else:
                for k in range(i, j):
                    dp[i][j] = dp[i][j] or (dp[i][k] and dp[k + 1][j])
    
    return dp[0][-1]

# Time Complexity = O((n ^ 2) * (n + m))
# Space Complexity = O(n ^ 2)