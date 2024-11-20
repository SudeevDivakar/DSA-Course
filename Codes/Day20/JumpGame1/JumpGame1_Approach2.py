def canJump(nums):
    #write code here
    goal = len(nums) - 1
    
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
            
    if goal != 0:
        return False
    else:
        return True


# Time Complexity = O(n)
# Space Complexity = O(1)