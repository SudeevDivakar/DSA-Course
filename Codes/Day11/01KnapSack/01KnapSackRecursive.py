def knapSack(W, wt, val, n):
    #write code here
    
    def helper(i, rem_weight):
        if i > n - 1 or rem_weight == 0:
            return 0
            
        exclude = helper(i + 1, rem_weight)
        include = 0
        if wt[i] <= rem_weight:
            include = val[i] + helper(i + 1, rem_weight - wt[i])
        
        return max(exclude, include)
    
    return helper(0, W)
    
    
# Time Complexity = O(2 ^ n)
# Space Complexity = O(n)