# Recursive Approach

def search_in_matrix(matrix,target):
    #write your code here
    
    def helper(start, end, nums, layer):
        middle = (start + end) // 2
        
        if layer == 1:
            if start > end:
                return False
            if target >= nums[middle][0] and target <= nums[middle][-1]:
                return helper(0, len(nums[middle]) - 1, nums[middle], 2)
            elif target < nums[middle][0]:
                return helper(start, middle - 1, nums, 1)
            else:
                return helper(middle + 1, end, nums, 1)
        
        if layer == 2:
            if start > end:
                return False
            if target == nums[middle]:
                return True
            elif target < nums[middle]:
                return helper(start, middle - 1, nums, 2)
            else:
                return helper(middle + 1, end, nums, 2)
            
    return helper(0, len(matrix) - 1, matrix, 1)
    

# Time Complexity = O(log m*n)
# Space Complexity = O(log m*n)