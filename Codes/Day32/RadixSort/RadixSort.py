def radix_sort(array):
    if len(array) == 0:
        return []
        
    num_count = len(str(max(array)))
    
    for i in range(num_count):
        counting_sort(array, i)
        
    #write code
    return array

def counting_sort(array, place):
    #write code
    output = [0] * len(array)
    cumulative_frequency = [0] * 10  # base 10
    digit_place = 10 ** place
    
    for i in array:
        digit = (i // digit_place) % 10
        cumulative_frequency[digit] += 1
        
    for i in range(len(cumulative_frequency) - 1):
        cumulative_frequency[i + 1] += cumulative_frequency[i]
    
    for i in range(len(array) - 1, -1, -1):
        curr_digit = (array[i] // digit_place) % 10
        cumulative_frequency[curr_digit] -= 1
        output[cumulative_frequency[curr_digit]] = array[i]
        
    array[:] = output


# Time Complexity = O(d * (n + k)) where d is the number of max digits in the array and k is the range of digits
# Space Complexity = O(n + k) where k is the range of digits
