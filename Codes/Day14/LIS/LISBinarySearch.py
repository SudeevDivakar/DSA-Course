def binary_search_index(temp, num):
    start, end = 0, len(temp) - 1
    
    while start < end:
        mid = (start + end) // 2
        if temp[mid] >= num:
            end = mid
        else:
            start = mid + 1
    
    return start

def lengthOfLIS(nums):
    #write code here
    n = len(nums)
    temp = [nums[0]]
    
    for i in range(1, n):
        if nums[i] > temp[-1]:
            temp.append(nums[i])
        else:
            ind = binary_search_index(temp, nums[i])
            temp[ind] = nums[i]
    
    return len(temp)

# Time Complexity = O(n * log n)
# Space Complexity = O(n)