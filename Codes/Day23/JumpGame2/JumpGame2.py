def jump(nums):
    #write code here
    res = 0
    
    l = r = 0
    
    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])
        
        res += 1
        l = r + 1
        r = farthest
    
    return res

# Time Complexity = O(n)
# Space Complexity = O(1)