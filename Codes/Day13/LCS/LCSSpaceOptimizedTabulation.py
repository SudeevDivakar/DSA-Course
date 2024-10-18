def longestCommonSubsequence(text1, text2):
    #write code here
    if len(text1) > len(text2):
        text1, text2 = text2, text1
        
    n = len(text1)
    m = len(text2)
    
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[j - 1] == text2[i - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
                
        prev = list(curr)
                
    return curr[-1]
    
# Time Complexity = O(n * m)
# Space Complexity = O(min(n, m))