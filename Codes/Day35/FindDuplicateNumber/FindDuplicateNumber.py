def getDuplicate(nums):
    #write your code here
    if len(nums) == 2:
        return nums[0]
        
    hare = 0
    tortoise = 0
    
    while True:
        hare = nums[nums[hare]]
        tortoise = nums[tortoise]
        
        if hare == tortoise:
            pointer = 0
            while pointer != tortoise:
                pointer = nums[pointer]
                tortoise = nums[tortoise]
                if pointer == tortoise:
                    return pointer

    
# Time Complexity = O(n)
# Space Complexity = O(1)