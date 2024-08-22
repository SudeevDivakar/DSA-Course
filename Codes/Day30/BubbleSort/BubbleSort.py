def bubble_sort(array):
    #write your code here
    sorted = False
    i = 0
    while sorted == False:
        sorted = True
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                sorted = False
        i += 1
        
    return array

# Time Complexity = O(n ^ 2)
# Space Complexity = O(1)