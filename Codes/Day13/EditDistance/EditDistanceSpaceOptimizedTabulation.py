def minDistance(word1, word2):
    #write code here
    if len(word2) > len(word1):
        word1, word2 = word2, word1
        
    n = len(word1)
    m = len(word2)
    
    prev = [i for i in range(m + 1)]
    
    curr = [0] * (m + 1)
    
    for i in range(1, n + 1):
        curr[0] = i
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]
                
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
                
        prev = list(curr)
        
    return curr[-1]
    
# Time Complexity = O(n * m)
# Space Complexity = O(min(n,m))