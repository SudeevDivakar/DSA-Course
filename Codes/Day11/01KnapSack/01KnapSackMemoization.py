def knapSack(W, wt, val, n):
    #write code here
    dp = [[-1] * (W + 1) for _ in range(n)]
    
    def helper(i, rem_weight):
        if i > n - 1 or rem_weight == 0:
            return 0
            
        if dp[i][rem_weight] != -1:
            return dp[i][rem_weight]
            
        exclude = helper(i + 1, rem_weight)
        include = 0
        if wt[i] <= rem_weight:
            include = val[i] + helper(i + 1, rem_weight - wt[i])
        
        dp[i][rem_weight] = max(exclude, include)
        return dp[i][rem_weight]
    
    return helper(0, W)
    

# Time Complexity = O(n * W)
# Space Complexity = O(n * W)