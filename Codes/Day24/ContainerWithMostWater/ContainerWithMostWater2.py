def max_area(array):
    #write code here
    
    volumes = []
    
    start = 0
    end = len(array) - 1
    
    while start <= end:
        if array[start] <= array[end]:
            volumes.append(array[start] * (end - start))
            start += 1
        else:
            volumes.append(array[end] * (end - start))
            end -= 1
            
    if len(volumes) == 0:
        return 0
    else:
        return max(volumes)
                
print([1,8,6,2,5,4,8,3,7])

# Time Complexity = O(n)
# Space Complexity = O(1)