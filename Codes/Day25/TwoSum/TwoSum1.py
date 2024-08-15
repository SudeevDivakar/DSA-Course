# Brute Force

def two_sum(array,target):
    #write code here
    if len(array) < 2:
        return []
        
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                return [i, j]
    
    return []

# Time Complexity = O(n ^ 2)
# Space Complexity = O(1)