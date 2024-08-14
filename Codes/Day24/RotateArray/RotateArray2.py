def rotate_array(array, k):
    if len(array) == 0:
        return []
    
    k = k % len(array)

    temp = array[-k:]

    for i in range(0, len(array)-k):
        array[i + k] = array[i]
    
    for i in range(len(temp)):
        array[i] = temp[i]
    
    return array

print(rotate_array([1, 2, 3, 4, 5], 3))

# Time Complexity = O(n)
# Space Complexity = O(k)