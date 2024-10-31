def minCut(s):
    #write code here
    n = len(s)
    
    isPalindrome = [[0] * n for _ in range(n)]
    
    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            
            if i == j:
                isPalindrome[i][j] = True
                
            elif s[i] == s[j] and (j == i + 1 or isPalindrome[i + 1][j - 1]):
                isPalindrome[i][j] = True
                
            else:
                isPalindrome[i][j] = False
    
    dp = [[None] * n for _ in range(n)]
    
    def helper(start, end):
        # base case
        if start == end or isPalindrome[start][end]:
            return 0
            
        if dp[start][end] != None:
            return dp[start][end]
            
        
        # recursive case
        minimum = end - start
        
        for i in range(start, end):
            if isPalindrome[start][i]:
                minimum = min(minimum, 1 + helper(i + 1, end))
                
        dp[start][end] = minimum
        return dp[start][end]
        
    return helper(0, n - 1)
                
    
# Time Complexity = O(n ^ 2)
# Space Complexity = O(n ^ 2)