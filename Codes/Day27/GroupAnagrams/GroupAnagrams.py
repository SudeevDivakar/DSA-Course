def group_anagrams(strings):
    #write your code here
    hashTable = {}
    sorted_strings = [''.join(sorted(i)) for i in strings]
    
    for i in range(len(sorted_strings)):
        if sorted_strings[i] not in hashTable:
            hashTable[sorted_strings[i]] = [strings[i]]
        else:
            hashTable[sorted_strings[i]].append(strings[i])
            
    return list(hashTable.values())
    

print(group_anagrams(['arc', 'abc', 'car', 'cat', 'act', 'acb', 'atc']))

# Time Complexity = O(s * nlogn) where s is the number of strings and n is the maximum number of characters in a string
# Space Complexity = O(s * n)