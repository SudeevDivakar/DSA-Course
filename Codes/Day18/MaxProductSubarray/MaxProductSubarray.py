def maxProduct(nums):
    #Write code here
    res = max(nums)
    
    currMax, currMin = 1, 1 
    
    for i in nums:
        temp = currMax
        
        currMax = max(i * currMax, i * currMin, i)
        currMin = min(i * temp, i * currMin, i)
        
        res = max(res, currMax)
    
    return res

# Time Complexity = O(n)
# Space Complexity = O(1)