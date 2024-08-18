# Iterative Approach

def binary_search(array,target):
    #write your code here
    
    start, end = 0, len(array) - 1
    
    while start <= end:
        
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            end = mid - 1
            
        elif array[mid] < target:
            start = mid + 1
    
    return -1

# Time Complexity = O(log n)
# Space Complexity = O(1)
