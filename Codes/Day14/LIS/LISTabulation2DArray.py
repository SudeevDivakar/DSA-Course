def lengthOfLIS(nums):
    #write code here
    n = len(nums)
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -2, -1):
            exclude = dp[i + 1][j + 1]
            include = 0
            if j == -1 or nums[i] > nums[j]:
                include = 1 + dp[i + 1][i + 1]
                
            dp[i][j + 1] = max(include, exclude)
            
    return dp[0][0]

# Space Complexity = O(n ^ 2)
# Time Complexity = O(n ^ 2)