def combinationSum2(candidates, target):
    #write code here
    
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
            hashTable = {}
            for j in range(i, n):
                if candidates[j] not in hashTable:
                    hashTable[candidates[j]] = True
                    subset.append(candidates[j])
                    helper(j + 1, sum_subset + candidates[j])
                    subset.pop()
            
    helper(0, 0)
    
    return combinations
    
    
print(combinationSum2([3,5,2,1,3], 7))

# Time Complexity = O(2 ^ n)
# Space Complexity = O(n) 