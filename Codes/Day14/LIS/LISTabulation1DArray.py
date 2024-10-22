def lengthOfLIS(nums):
    #write code here
    n = len(nums)
    
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    
    return max(dp)

# Time Complexity = O(n ^ 2)
# Space Complexity = O(n)