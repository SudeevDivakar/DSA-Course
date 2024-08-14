def rotate_array(array,k):
    #write code here
    
    return array[len(array) - k:] + array[:len(array) - k]

print(rotate_array([1, 2, 3, 4, 5], 3))

# Time Complexity = O(n)
# Space Complexity = O(n)

# We can try and implement this with a constant space complexity instead