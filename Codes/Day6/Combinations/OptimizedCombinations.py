def combine(n,k):
    #write code here
    
    nums = list(range(n))
    
    combinations = []
    subset = []
    def helper(i):
        if len(subset) == k:
            combinations.append(list(subset))
        else:
            need = k - len(subset)
            for j in range(i, n-(need-1)+1):
                subset.append(j)
                helper(j + 1)
                subset.pop()
    
    helper(1)
    
    return combinations
    
print(combine(4,3))
