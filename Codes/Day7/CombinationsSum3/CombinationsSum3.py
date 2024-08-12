def combinationSum3(k, n):
    #write code here
    
    combinations = []
    subset = []
    
    def helper(i, sum_subset):
        if len(subset) == k and sum_subset == n:
            combinations.append(list(subset))
        
        elif sum_subset > n:
            return
            
        else:
            for j in range(i, 10):
                subset.append(j)
                helper(j + 1, sum_subset + j)
                subset.pop()
            
        
    helper(1, 0)
    
    return combinations
    
print(combinationSum3(3, 6))