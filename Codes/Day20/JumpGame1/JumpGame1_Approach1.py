def canJump(nums):
    #write code here
    n = len(nums)
    reach = 0
    
    for i in range(n):
        if i > reach:
            return False
        
        curr = i + nums[i]
        if curr > reach:
            reach = curr
        
        if reach >= n - 1:
            return True
    
    return False
    
    
# Time Complexity = O(n)
# Space Complexity = O(1)