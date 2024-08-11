def subsetsWithDup(nums):
    #write code here
    
    nums.sort()
    
    powerset = []
    subset=[]
    def helper(i):
        if i == len(nums):
            powerset.append(list(subset))
        else:
            subset.append(nums[i])
            helper(i + 1)
            subset.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1)
        
    helper(0)
    
    return powerset
    
print(subsetsWithDup([1,3,3,7]))                  

# Time Complexity = O(n * 2^n)
# Space Complexity = O(n)