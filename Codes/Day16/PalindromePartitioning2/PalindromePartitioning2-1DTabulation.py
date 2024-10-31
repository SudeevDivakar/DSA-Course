def minCut(s):
    #write code here
    n = len(s)
    
    isPalindrome = [[False] * n for _ in range(n)]
    
    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            
            if i == j:
                isPalindrome[i][j] = True
                
            elif s[i] == s[j] and (j == i + 1 or isPalindrome[i + 1][j - 1]):
                isPalindrome[i][j] = True
                
    dp = [0] * n
    
    for end in range(n):
        min_cuts = end
        for start in range(end + 1):
            if isPalindrome[start][end]:
                if start == 0:
                    min_cuts = 0
                else:
                    min_cuts = min(min_cuts, 1 + dp[start - 1])
        
        dp[end] = min_cuts
    
    return dp[-1]
                
# Time Complexity = O(n ^ 2)
# Space Complexity = O(n ^ 2)