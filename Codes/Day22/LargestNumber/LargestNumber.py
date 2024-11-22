from functools import cmp_to_key

def largestNumber(nums):
    #write code here
    for i in range(len(nums)):
        nums[i] = str(nums[i])
    
    def compare(n1, n2):
        if n1 + n2 > n2 + n1:
            return -1
        else:
            return 1
        
    nums.sort(key=cmp_to_key(compare))

    return str(int(''.join(nums)))
        
# Time Complexity = O(n * k * log n)
# Space Complexity = O(n + k)