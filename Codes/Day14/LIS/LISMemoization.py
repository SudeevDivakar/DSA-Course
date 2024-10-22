def lengthOfLIS(nums):
    #write code here
    n = len(nums) - 1
    
    dp = {}
    
    def helper(prev, curr):
        if curr > n:
            return 0
        
        if (prev, curr) in dp:
            return dp[(prev, curr)]
            
        if prev == -1 or nums[curr] > nums[prev]:
            include = 1 + helper(curr, curr + 1)
            
        else:
            include = 0
            
        exclude = helper(prev, curr + 1)
        
        dp[(prev, curr)] = max(include, exclude)
        return dp[(prev, curr)]
    
    return helper(-1, 0)


# Time Complexity = O(n ^ 2)
# Space Complexity = O(n ^ 2) 