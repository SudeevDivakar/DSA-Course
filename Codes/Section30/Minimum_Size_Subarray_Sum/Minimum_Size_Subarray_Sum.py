def minSubArrayLen(target, nums):
    #write code here 
    curr = 0
    res = float('inf')
    
    l = 0
    for r in range(len(nums)):
        curr += nums[r]
        
        while curr >= target:
            size = r - l + 1
            if size < res:
                res = size
            
            curr -= nums[l]
            
            l += 1
    
    if res == float('inf'):
        return 0
    else:
        return res
            

# Time Complexity = O(n)
# Space Complexity = O(1)