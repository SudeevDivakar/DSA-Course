def sorted_squared(array):
    #write code here.make sure to return desired array
    left = 0
    end_pointer = right = len(array) - 1
    
    new_array = [0] * len(array)
    
    while(left <= right):
        if((array[right]) ** 2 > (array[left]) ** 2):
            new_array[end_pointer] = (array[right]) ** 2
            end_pointer -= 1
            right -= 1
        else:
            new_array[end_pointer] = (array[left]) ** 2
            end_pointer -= 1
            left += 1
    
    return new_array

sorted_squared([-5, -3, -1, 0, 1, 2, 4, 6])