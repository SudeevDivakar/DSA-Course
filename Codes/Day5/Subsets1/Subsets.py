def power_set (nums):
    #write code here
    
    powerset = []
    subset = []
    def helper(i):
        if i == len(nums):
            powerset.append(list(subset))
        else:
            helper(i + 1)
            subset.append(nums[i])
            helper(i + 1)
            subset.pop()
        
    helper(0)
    
    return powerset
    
print(power_set([1,2,3]))

# Time Complexity = O(n * 2^n)
# Space Complexity = O(n)