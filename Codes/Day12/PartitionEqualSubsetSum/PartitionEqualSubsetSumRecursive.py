def canPartition(nums):
    #Write code here
    sum_list = sum(nums)
    if sum_list % 2 != 0:
        return False
        
    sum_target = sum_list / 2
    
    def helper(i, target):
        if target == 0:
            return True
        
        if target < 0 or i > len(nums) - 1:
            return False
        
        include = helper(i + 1, target - nums[i])
        exclude = helper(i + 1, target)
        
        return include or exclude
        
    return helper(0, sum_target)
        

# Time Complexity = O(2 ^ n)
# Space Complexity = O(n)