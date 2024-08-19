# Recursive Approach

def search_for_range(array,target):
    #write your code here

    result = [-1, -1]
    
    def helper_first(start, end):
        middle = (start + end) // 2
        
        if start > end:
            return
        
        if array[middle] == target:
            if middle == 0 or array[middle - 1] != array[middle]:
                result[0] = middle
                return
            else:
                return helper_first(start, middle - 1)
            
        elif target > array[middle]:
            return helper_first(middle + 1, end)
        
        else:
            return helper_first(start, middle - 1)
            
        
    def helper_last(start, end):
        middle = (start + end) // 2
        
        if start > end:
            return
        
        if array[middle] == target:
            if middle == len(array) - 1 or array[middle] != array[middle + 1]:
                result[1] = middle
                return
            else:
                return helper_last(middle + 1, end)
        
        elif target > array[middle]:
            return helper_last(middle + 1, end)
        
        else:
            return helper_last(start, middle - 1)
    
    helper_first(0, len(array) - 1)
    helper_last(0, len(array) - 1)
                
    return result  
                
                
# Time Complexity = O(log n)
# Space Complexity = O(log n)