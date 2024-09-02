# With Sorting the Array

def threeSum(nums):
    #Write code here
    nums = sorted(nums)
    res = []
    
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]: 
            start = i + 1
            end = len(nums) - 1
            
            while start < end:
                sumThree = nums[i] + nums[start] + nums[end]
                if sumThree == 0:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                elif sumThree > 0:
                    end -= 1
                else:
                    start += 1
    
    
    return res

# Time Complexity = O(n ^ 2)
# Space Complexity (Depends on sorting Algorithm)
# O(1) in the case of heap sort and O(n) in the case of merge sort.  