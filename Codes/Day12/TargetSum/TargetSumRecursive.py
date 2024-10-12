def findTargetSumWays(nums, target):
    #Write code here
    def helper(i, total):
        if i == len(nums):
            if total == target:
                return 1
            else:
                return 0
            
        left = helper(i + 1, total + nums[i])
        right = helper(i + 1, total - nums[i])
        
        return left + right
        
    return helper(0, 0)

# Time Complexity = O(2 ^ n)
# Space Complexity = O(n)