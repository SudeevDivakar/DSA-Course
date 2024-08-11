# Find all the different permutations for a list of non-repeating integers

def permute(nums):
    #write code here 
    permutations = []
    def helper(i):
        if i == len(nums) - 1:
            permutations.append(list(nums))
        else:
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                helper(i+1)
                nums[i], nums[j] = nums[j], nums[i]
            
    helper(0)
    
    return permutations
    
print(permute([1,4,5]))
    
# Space Complexity = O(n * n!)
# Time Complexity = O(n * n!)