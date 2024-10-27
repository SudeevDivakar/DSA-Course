def countPalin(l, r, s):
    n = len(s)
    res = 0
    
    while l >= 0 and r < n and s[l] == s[r]:
        res += 1
        l -= 1
        r += 1
        
    return res
    
def countSubstrings(s):
    #write code here
    n = len(s)
    
    res = 0
    
    for i in range(n):
        res += countPalin(i, i, s)
        res += countPalin(i, i + 1, s)
    
    return res
    

# Time Complexity = O(n ^ 2)
# Space Complexity = O(1)