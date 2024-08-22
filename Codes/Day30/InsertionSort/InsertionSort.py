def insertion_sort(array):
    #write your code here
    for i in range(1, len(array)):
        insert_element = array[i]
        j = i - 1
        
        while j > -1 and array[j] > insert_element:
            array[j + 1] = array[j]
            j -= 1
            
        array[j + 1] = insert_element
               
    return array

# Time Complexity = O(n)   (best case)
# Time Complexity = O(n ^ 2)  (avg and worst)
# Space Complexity = O(1)