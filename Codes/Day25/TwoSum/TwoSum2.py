# Hash Table Method

def two_sum(array,target):
    #write code here
    if len(array) < 2:
        return []
        
    hashTable = {}
    
    for i in range(len(array)):
        check = target - array[i]
        if check not in hashTable:
            hashTable[array[i]] = i
        else:
            return [hashTable[check], i]
        
    return []

# Time Complexity = O(n)
# Space Complexity = U(n)