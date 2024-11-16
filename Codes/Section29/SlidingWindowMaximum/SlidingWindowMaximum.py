from collections import deque
def maxSlidingWindow(nums, k):
    #write code here
    queue = deque([0])
    
    for i in range(1, k):
        while len(queue) > 0 and nums[i] > nums[queue[-1]]:
            queue.pop()
            
        queue.append(i)
    
    output = [nums[queue[0]]]
    
    for i in range(k, len(nums)):
        if queue[0] == i - k:
            queue.popleft()
            
        while len(queue) > 0 and nums[i] > nums[queue[-1]]:
            queue.pop()
        
        queue.append(i)
        
        output.append(nums[queue[0]])
    
    return output
        
    
# Time Complexity = O(n)
# Space Complexity = O(k)