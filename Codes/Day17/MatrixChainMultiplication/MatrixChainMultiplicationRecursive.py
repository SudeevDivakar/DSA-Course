def matrixMultiplication(N, arr):
    #Write code here
    def helper(i, j):
        if i == j:
            return 0
        
        cost = float('inf')
        for k in range(i, j):
            curr_cost = helper(i, k) + helper(k + 1, j) + (arr[i - 1] * arr[k] * arr[j])
            cost = min(cost, curr_cost)
        
        return cost
        
    return helper(1, N - 1)
    

# Time Complexity = O((2 ^ n) * n)
# Space Complexity = O(n)