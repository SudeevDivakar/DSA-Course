# Find all the different permutations for a list of non-repeating integers

def permute(nums):
    #write code here 
    permutations = []
    def helper(i):
        nonlocal permutations
        if i == len(nums) - 1:
            if nums not in permutations:
                permutations.append(list(nums))
        else:
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                helper(i+1)
                nums[i], nums[j] = nums[j], nums[i]    #backtracking step (done because changes to the state of the problem are done in place)
            
    helper(0)
    
    return permutations
    
print(permute([1,4,5]))
    

# Space Complexity = O(n)
# Time Complexity = O(n * n!)