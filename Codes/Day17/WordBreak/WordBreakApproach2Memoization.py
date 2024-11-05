def wordBreak(s, wordDict):
    #Write code here
    n = len(s)
    
    dp = [-1] * n
    
    def check(index):
        if index < 0:
            return True
        
        if dp[index] != -1:
            return dp[index]
        
        for word in wordDict:
            if s[index - len(word) + 1: index + 1] == word and check(index - len(word)):
                dp[index] = True
                return True
        
        return False
    
    return check(n - 1)
    
# Time Complexity = O(n * m * k) where n -> maximum number of calls to check function, m -> traversing wordDict array/list, k -> making substring for checking
# Space Complexity = O(n)