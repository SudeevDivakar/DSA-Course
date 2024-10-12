def canPartition(nums):
    #Write code here
    sum_list = sum(nums)
    if sum_list % 2 != 0:
        return False
        
    sum_target = sum_list / 2
    
    dp = {}
    
    def helper(i, target):
        if target == 0:
            return True
        
        if target < 0 or i > len(nums) - 1:
            return False
            
        if (i, target) in dp:
                return dp[(i, target)]
        
        include = helper(i + 1, target - nums[i])
        exclude = helper(i + 1, target)
        
        dp[(i, target)] = include or exclude
        return dp[(i, target)]
        
    return helper(0, sum_target)
        
            
# Time Complexity = O(n * sum(nums))
# Space Complexity = O(n * sum(nums))