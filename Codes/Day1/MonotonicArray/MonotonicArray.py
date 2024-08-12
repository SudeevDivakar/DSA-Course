def monotonic_array(array):
    #write code here
    left = 0
    right = len(array) - 1
    
    if(len(array) == 0 or len(array) == 1):
        return True
    
    while(left < right):
        if(array[0] < array[-1]):
            if(array[left] <= array[left+1] and array[right] >= array[right-1]):
                left += 1
                right -= 1
            else:
                return False
        else:
            if(array[left] >= array[left+1] and array[right] <= array[right-1]):
                left += 1
                right -= 1
            else:
                return False
    return True
        
            
