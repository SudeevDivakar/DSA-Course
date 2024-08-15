def isomorphic_strings(s, t):
    #write code here
    if len(s) != len(t):
        return False
        
    hashTable_s = {}
    hashTable_t = {}
    
    for i in range(len(s)):
        if s[i] not in hashTable_s:
            if t[i] not in hashTable_t:
                hashTable_t[t[i]] = s[i]
                hashTable_s[s[i]] = t[i]
            else:
                return False
        else:
            if hashTable_s[s[i]] != t[i]:
                return False
                
    return True

# Time Complexity = O(n)
# Space Complexity = O(1)