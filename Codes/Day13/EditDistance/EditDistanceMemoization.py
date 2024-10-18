def minDistance(word1, word2):
    #write code here
    dp = {}
    
    def helper(i, j):
        if i > len(word1) - 1:
            return len(word2) - j
            
        if j > len(word2) - 1:
            return len(word1) - i
            
        if (i, j) in dp:
            return dp[(i, j)]
        
        if word1[i] == word2[j]:
            dp[(i, j)] = helper(i + 1, j + 1)
        else:
            insertion = 1 + helper(i, j + 1)
            deletion = 1 + helper(i + 1, j)
            replace = 1 + helper(i + 1, j + 1)
        
            dp[(i, j)] = min(insertion, deletion, replace)
        
        return dp[(i, j)]
        
    return helper(0, 0)
    
    
    
# Time Complexity = O()
# Space Complexity = O(n * m)