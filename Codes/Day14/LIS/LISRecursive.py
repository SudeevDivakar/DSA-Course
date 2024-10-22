def lengthOfLIS(nums):
    #write code here
    n = len(nums) - 1
    
    def helper(prev, curr):
        if curr > n:
            return 0
        
        if prev == -1 or nums[curr] > nums[prev]:
            include = 1 + helper(curr, curr + 1)
        else:
            include = 0
            
        exclude = helper(prev, curr + 1)
        
        return max(include, exclude)
        
    return helper(-1, 0)


# Time Complexity = O(2 ^ n)
# Space Complexity = O(n)