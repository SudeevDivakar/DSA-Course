def search_rotated_sorted_array(nums,target):
    #write your code here
    
    start, end = 0, len(nums) - 1
    
    while start <= end:
        middle = (start + end) // 2
        
        if nums[middle] == target:
            return middle
            
        elif nums[start] <= nums[middle]:
            if target >= nums[start] and target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1
            
        else:
            if target > nums[middle] and target <= nums[end]:
                start = middle + 1
            else:
                end = middle - 1
        
                
    return -1


# Time Complexity = O(log n)
# Space Complexity = O(1) because it's iterative ( O(log n) is it's recursive )