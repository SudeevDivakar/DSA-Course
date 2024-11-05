def maxSubArray(nums):
    #write code here
    max_sum = -float('inf')
    curr_sum = 0
    
    for i in nums:
        curr_sum += i
        if curr_sum > max_sum:
            max_sum = curr_sum
        
        if curr_sum < 0:
            curr_sum = 0
    
    return max_sum

# Time Complexity = O(n)
# Space Complexity = O(1)