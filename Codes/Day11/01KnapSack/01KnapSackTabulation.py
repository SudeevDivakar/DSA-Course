def knapSack(W, wt, val, n):
    #write code here
    dp = [[0] * (W + 1) for _ in range(n + 1)]  
    
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            exclude = dp[i - 1][j]
            include = 0
            if wt[i - 1] <= j:
                include = val[i - 1] + dp[i - 1][j - wt[i - 1]]
            dp[i][j] = max(exclude, include)
            
    return dp[-1][-1]

# Time Complexity = O(n * W)
# Space Complexity = O(n * W) - Space occupied by DP table