def rotate_array(nums,k):
    #write code here
    
    if len(nums) == 0:
        return []
    
    k = k % len(nums)
    
    nums.reverse()
    
    i, j = 0, k - 1
    start, end = k, len(nums) - 1
    
    while i <= j or start <= end:
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        if start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1 
            end -= 1
            
            
    return nums

print(rotate_array([1, 2, 3, 4, 5], 3))

# Time Complexity = O(n)
# Space Complexity = O(1)