def findTargetSumWays(nums, target):
    #Write code here
    dp = {}
    
    def helper(i, total):
        if i == len(nums):
            if total == target:
                return 1
            else:
                return 0
                
        if (i, total) in dp:
            return dp[(i, total)]
            
        left = helper(i + 1, total + nums[i])
        right = helper(i + 1, total - nums[i])
        
        dp[(i, total)] = left + right
        
        return dp[(i, total)]
        
    return helper(0, 0)

# Time Complexity = O(n)
# Space Complexity = O(n)