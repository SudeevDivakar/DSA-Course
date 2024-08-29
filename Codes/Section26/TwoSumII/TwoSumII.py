def twoSum(numbers, target):
    #write code here 
    left = 1
    right = len(numbers)
    
    while True:
        if numbers[left - 1] + numbers[right - 1] == target:
            return [left, right]
        elif numbers[left - 1] + numbers[right - 1] > target:
            right -= 1
        else:
            left += 1


# Time Complexity = O(n)
# Space Complexity = O(1)