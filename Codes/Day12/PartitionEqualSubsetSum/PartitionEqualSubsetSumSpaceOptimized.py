def canPartition(nums):
    #Write code here
    sum_list = sum(nums)
    if sum_list % 2 != 0:
        return False
        
    sum_target = sum_list / 2
    
    dp = set()
    dp.add(0)
    
    for i in range(len(nums)):
        nextDP = set()
        for j in dp:
            if j + nums[i] == sum_target:
                return True
            nextDP.add(j + nums[i])
            nextDP.add(j)
        dp = nextDP
    
    if sum_target not in dp:
        return False
    

# Time Complexity = O(n * sum(nums))
# Space Complexity = O(sum(nums))