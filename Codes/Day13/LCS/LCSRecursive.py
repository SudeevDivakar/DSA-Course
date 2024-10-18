def longestCommonSubsequence(text1, text2):
    #write code here
    
    def helper(i, j):
        if i > len(text1) - 1 or j > len(text2) - 1:
            return 0
        
        if text1[i] == text2[j]:
            return 1 + helper(i + 1, j + 1)
        
        else:
            return max(helper(i + 1, j), helper(i, j + 1))
    
    return helper(0, 0)

# Time Complexity = O(2 ^ (n + m))
# Space Complexity = O(n + m)