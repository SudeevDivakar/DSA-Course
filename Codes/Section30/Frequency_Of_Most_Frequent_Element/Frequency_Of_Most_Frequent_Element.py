def maxFrequency(nums, k):
    #write code here
    nums.sort()
    
    curr = 0
    freq = 0
    l = 0
    for r in range(len(nums)):
        curr += nums[r]
        
        while curr + k < nums[r] * (r - l + 1):
            curr -= nums[l]
            l += 1
        
        freq = max(freq, r - l + 1)
        
    return freq
        
# Time Complexity = O(n * log n)
# Space Complexity = O(n)  or  O(log n)  based on sorting algorithm used