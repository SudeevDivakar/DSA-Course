# HashTable Method 

def non_repeating_char(str):
    ht = {}

    for i in str:
        if i not in ht:
            ht[i] = 1
        else:
            ht[i] += 1
    
    for i in range(len(str)):
        if ht[str[i]] == 1:
            return i
    
    return None

# Time Complexity = O(n)
# Space Complexity = O(1) because hashTable can store at max 62 characters (lowercase, uppercase and integers from 0-9)