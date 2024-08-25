def merge_arrays(left_side, right_side):
    merged_array = []
    i, j = 0, 0
    
    while i < len(left_side) and j < len(right_side):
        if left_side[i] <= right_side[j]:
            merged_array.append(left_side[i])
            i += 1
        else:
            merged_array.append(right_side[j])
            j += 1

    while i < len(left_side):
        merged_array.append(left_side[i])
        i += 1
    
    while j < len(right_side):
        merged_array.append(right_side[j])
        j += 1

    return merged_array
    
def merge_sort(array):
    #write your code here
    if len(array) <= 1:
        return array
        
    middle = len(array) // 2
    left_array = merge_sort(array[:middle])
    right_array = merge_sort(array[middle:])
    
    return merge_arrays(left_array, right_array)


# Time Complexity = O(n * log n)
# Space Complexity = O(n)