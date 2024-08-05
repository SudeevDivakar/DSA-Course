def sorted_squared(array):
    #write code here.make sure to return desired array
    if(len(array) == 0):
        return []
    
    for i in range(len(array)):
        array[i] = (array[i]) ** 2
        
    array.sort()
    
    return array

print(sorted_squared([-4 ,-2, -1, 0, 1, 2, 3, 4]))
    