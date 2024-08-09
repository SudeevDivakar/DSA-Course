# Find all the different unique permutations for a list of repeating integers

def permuteUnique(nums):
    #write code here
    
    permutations = []
    def helper(i):
        for j in range(i, len(nums)):
            if i == len(nums) - 1:
                if nums not in permutations:
                    permutations.append(list(nums))
            else:
                nums[i], nums[j] = nums[j], nums[i]
                helper(i+1)
                nums[i], nums[j] = nums[j], nums[i]
           
                
    helper(0)
        
    return permutations
        
print(permuteUnique([3,3,2]))

# Space Complexity = O(n)
# Time Complexity = O(n * n!)