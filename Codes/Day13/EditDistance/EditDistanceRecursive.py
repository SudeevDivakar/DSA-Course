def minDistance(word1, word2):
    #write code here
    def helper(i, j):
        if i > len(word1) - 1:
            return len(word2) - j
            
        if j > len(word2) - 1:
            return len(word1) - i
        
        if word1[i] == word2[j]:
            return helper(i + 1, j + 1)
        
        insertion = 1 + helper(i, j + 1)
        deletion = 1 + helper(i + 1, j)
        replace = 1 + helper(i + 1, j + 1)
        
        return min(insertion, deletion, replace)
        
    return helper(0, 0)
    
# Time Complexity = O(3 ^ (n + m))
# Space Complexity = O(n + m)