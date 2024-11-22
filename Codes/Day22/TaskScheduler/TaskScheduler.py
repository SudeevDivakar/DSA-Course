def leastInterval(tasks, n):
    #write code here
    t = len(tasks)
    count = [0] * 26
    max_freq = 0
    number_max_freq = 0
     
    for task in tasks:
        idx = ord(task) - ord('A')
        count[idx] += 1
         
        if max_freq < count[idx]:
            max_freq = count[idx]
            number_max_freq = 1
            
        elif max_freq == count[idx]:
            number_max_freq += 1
    
    parts = max_freq - 1
    slots_per_part = n - (number_max_freq - 1)
    slots = parts * slots_per_part
    remaining_tasks = t - (max_freq * number_max_freq)
    empty_slots = max(slots - remaining_tasks, 0)
    
    return t + empty_slots

# Time Complexity = O(n)
# Space Complexity = O(1)   (count array can be at max of size 26)