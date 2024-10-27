def maxPalidrome(l, r, s):
    n = len(s)
    res = ''
    resLen = 0
    
    while l >= 0 and r < n and s[l] == s[r]:
        if r - l + 1 > resLen:
            res = s[l : r + 1]
            resLen = r - l + 1
        l -= 1
        r += 1
        
    return res, resLen
    
def longestPalindrome(s):
    #Write code here
    n = len(s)
    res = ''
    resLen = 0
    
    
    for i in range(n):
        string1, string1Len = maxPalidrome(i, i, s)
        string2, string2Len = maxPalidrome(i, i + 1, s)
        if string1Len > string2Len and string1Len > resLen:
            resLen = string1Len
            res = string1
        elif string2Len >= string1Len and string2Len > resLen:
            resLen = string2Len
            res = string2
    
    return res
        
        
# Time Complexity = O(n ^ 2)
# Space Complexity = O(1)
