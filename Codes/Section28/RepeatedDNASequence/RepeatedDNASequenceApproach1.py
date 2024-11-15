def findRepeatedDnaSequences(s):
    # Given Length of a sequence = 10 
    L = 10
    #write code here
    seen = set()
    output = set()
    
    for i in range(len(s) - L + 1):
        seq = s[i : i + L]
        
        if seq in seen:
            output.add(seq)
            
        else:
            seen.add(seq)
    
    return list(output)

# Time Complexity = O((n - L) * L)
# Space Complexity = O(L * (n - L))