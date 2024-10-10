def knapSack(N, W, val, wt):
    #write code here
    prev = [0] * (W + 1)
    curr = [0] * (W + 1)
    
    for i in range(1, N + 1):
        for j in range(1, W + 1):
            exclude = prev[j]
            include = 0
            if wt[i - 1] <= j:
                include = val[i - 1] + curr[j - wt[i - 1]]
                
            curr[j] = max(include, exclude)
            
        prev = curr
            
    return curr[-1]
    
    
# Time Complexity = O(n * W)
# Space Complexity = O(W) - Space occupied by array