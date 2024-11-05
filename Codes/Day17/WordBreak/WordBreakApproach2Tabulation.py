def wordBreak(s, wordDict):
    #Write code here
    n = len(s)
    
    dp = [False] * n
    
    for i in range(n):
        for word in wordDict:
            if i < len(word) - 1:
                continue
            
            elif s[i - len(word) + 1 : i + 1] == word and (dp[i - len(word)] or i == len(word) - 1):
                dp[i] = True
    
    return dp[-1]

# Time Complexity = O(n * m * k) where n -> maximum number of calls to check function, m -> traversing wordDict array/list, k -> making substring for checking
# Space Complexity = O(n)