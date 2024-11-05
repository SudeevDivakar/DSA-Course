def matrixMultiplication(N, arr):
    #Write code here
    dp = [[0] * N for _ in range(N)]
    
    for l in range(1, N + 1):
        for i in range(1, N - l + 1):
            j = i + l - 1
            
            if i == j:
                dp[i][j] = 0
            
            else:
                cost = float('inf')
                for k in range(i, j):
                    new_cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                    cost = min(cost, new_cost)
                dp[i][j] = cost
    
    return dp[1][-1]
            
# Time Complexity = O(n ^ 3)
# Space Complexity = O(n ^ 2)