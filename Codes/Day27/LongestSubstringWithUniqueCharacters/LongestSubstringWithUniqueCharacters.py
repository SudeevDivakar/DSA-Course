def max_unique_length(str):
    #write your code here
    max_length = 0
    start = 0
    hashTable = {}
    
    for i in range(len(str)):
        if str[i] not in hashTable:
            hashTable[str[i]] = i
        
        else:
            start = max(start, hashTable[str[i]] + 1)
            hashTable[str[i]] = i
            
        length = i + 1 - start
        if length > max_length:
            max_length = length
        
    return max_length

# Time Complexity = O(n)
# Space Complexity = O(min(n, m)) where m is the number of unique strings