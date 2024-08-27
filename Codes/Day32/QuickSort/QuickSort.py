def swap(array, i, j):
    #write code to swap
    array[i], array[j] = array[j], array[i]

def partition(array, start=0, end=None):
    #write code
    if end == None:
        end = len(array) - 1
        
    middle = (start + end) // 2
    swap(array, start, middle)
    
    i = start + 1
    j = end
    
    while i <= j:
        while i <= j and array[i] <= array[start]:
            i += 1
        while i <= j and array[j] > array[start]:
            j -= 1
        if i < j:
            swap(array, i, j)
            
    swap(array, start, j)
    
    return j
        


def quick_sort(array, start=0, end=None):
    #write code
    if end == None:
        end = len(array) - 1
        
    while start < end:
        pivot_id = partition(array, start, end)
        
        if pivot_id - start < end - pivot_id:
            quick_sort(array, start, pivot_id - 1)
            start = pivot_id + 1
            
        else:
            quick_sort(array, pivot_id + 1, end)
            end = pivot_id - 1


# Time Complexity = O(n * logn) Best Case
# Time Complexity = O(n ^ 2) Worst Case

# Normal Space Complexity
# Space Complexity = O(n) Worst Case
# Space Complexity = O(logn) Best Case

# Sedwig's method
# Space Complexity = O(log n) Worst Case
# Space Complexity = O(1) Best Case