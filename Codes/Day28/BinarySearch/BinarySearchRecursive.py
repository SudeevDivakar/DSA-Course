# Recursive Approach

def binary_search(array,target):
    #write your code here
    
    start, end = 0, len(array) - 1
    
    def helper(start, end):
        middle = (start + end) // 2
        if start > end:
            return -1
        
        elif array[middle] == target:
            return middle
            
        elif array[middle] > target:
            return helper(start, middle - 1)
            
        elif array[middle] < target:
            return helper(middle + 1, end)
            
    return helper(start, end)

# Time Complexity = O(log n)
# Space Complexity = O(log n)