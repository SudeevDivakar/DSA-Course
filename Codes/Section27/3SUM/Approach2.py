# Without Sorting the Array

def threeSum(nums):
    #Write code here
    res = set()
    
    for i in range(len(nums)):
        j = i + 1
        need = set()
        
        while j < len(nums):
            check = nums[i] + nums[j]
            if -(check) not in need:
                need.add(nums[j])
            else:
                res.add(tuple(sorted([nums[i], nums[j], -(check)])))
            j += 1 
    
    final_res = [list(i) for i in res]
    
    return final_res

# Time Complexity = O(n ^ 2)
# Space Complexity = O(n)   Space taken up by the set  