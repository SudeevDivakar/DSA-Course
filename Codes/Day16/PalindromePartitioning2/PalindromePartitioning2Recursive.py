def minCut(s):
    #write code here
    n = len(s)
    
    def isPalindrome(i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True
    
    def helper(start, end):
        # base case
        if start == end or isPalindrome(start, end):
            return 0
        
        # recursive case
        minimum = end - start
        
        for i in range(start, end):
            if isPalindrome(start, i):
                minimum = min(minimum, 1 + helper(i + 1, end))
                
        return minimum
            
    return helper(0, n - 1)
                

# Time Complexity = O((2 ^ n) * n)
# Space Complexity = O(n ^ 2)