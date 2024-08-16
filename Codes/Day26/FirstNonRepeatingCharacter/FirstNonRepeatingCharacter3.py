# My solution (Should have a complexity of O(n^ 2) but is faster than the other two solutions somehow)

def non_repeating_char(str):
    #write code here
    
    hashMap = {}
    
    for i in range(len(str)):
        if str[i] not in hashMap:
            hashMap[str[i]] = True
            if str.count(str[i]) == 1:
                return i
    
    return None

# Time Complexity = O(n ^ 2)
# Space Complexity = O(1) because hashTable can store at max 62 characters (lowercase, uppercase and integers from 0-9)