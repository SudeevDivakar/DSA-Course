# Iterative Approach

def search_for_range(array,target):
    #write your code here

    start, end = 0, len(array) - 1
    result = [-1, -1]

    # Find first element
    while start <= end:
        middle = (start + end) // 2
        
        if array[middle] == target:
            if middle == 0 or array[middle - 1] != array[middle]:
                result[0] = middle
                break
            else:
                end = middle - 1
        
        elif target > array[middle]:
            start = middle + 1
            
        else:
            end = middle - 1
            
    # Find last element
    start, end = 0, len(array) - 1
    while start <= end:
        middle = (start + end) // 2
        
        if array[middle] == target:
            if middle == len(array) - 1 or array[middle + 1] != array[middle]:
                result[1] = middle 
                break
            else:
                start = middle - 1
        
        elif target > array[middle]:
            start = middle + 1
            
        else:
            end = middle - 1
                
    
    return result  
                
                
# Time Complexity = O(log n)
# Space Complexity = O(1)