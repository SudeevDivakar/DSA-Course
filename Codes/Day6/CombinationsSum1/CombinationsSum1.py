def combinationSum(candidates, target):
    #write code here
    #the integers in the candidates array are all non negative  
    
    candidates.sort()
    
    combinations = []
    subset = []
    
    n = len(candidates)
    
    def helper(i, sum_subset):
        if sum_subset == target:
            combinations.append(list(subset))
        elif sum_subset > target:
            return
        else:
            for j in range(i, n):
                subset.append(candidates[j])
                helper(j, sum_subset + candidates[j])
                subset.pop()
                
        
    helper(0, 0)
    
    return combinations
    
print(combinationSum([8,2,1,9], 9))


# Space Complexity = O(T / M), where T = Target value and M = Minimum candidate value in array
# Time Complexity = O(N ^ ((T / M) + 1)), where T = Target value, M = Minimum candidate value in array and N = Number of Candidates in array