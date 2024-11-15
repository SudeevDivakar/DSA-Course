def findMaxAverage(nums, k):
    #write code here
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, curr_sum)
    
    return max_sum / k

# Time Complexity = O(n)
# Space Complexity = O(1)