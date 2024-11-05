def matrixMultiplication(N, arr):
    #Write code here
    dp = [[-1] * N for _ in range(N)]
    
    def helper(i, j):
        if i == j:
            return 0
            
        if dp[i][j] != -1:
            return dp[i][j]
         
        cost = float('inf')
        for k in range(i, j):
            curr_cost = helper(i, k) + helper(k + 1, j) + (arr[i - 1] * arr[k] * arr[j])
            cost = min(cost, curr_cost)
        
        dp[i][j] = cost
        return dp[i][j]
        
    return helper(1, N - 1)

# Time Complexity = O(n ^ 3)
# Space Complexity = O(n ^ 2)