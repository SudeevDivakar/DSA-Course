def numRescueBoats(people, limit):
    #write code here
    i = 0
    j = len(people) - 1
    
    res = 0
    people.sort()
    
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        
        j -= 1
        res += 1
        
    return res

# Time Complexity = O(n * log n)
# Space Complexity = O(n) / O(log n)   -> based on sorting algorithm used