def merge(intervals):
    #write code here
    n = len(intervals)
    intervals.sort()
    
    res = [intervals[0]]
    
    for i in range(1, n):
        if res[-1][1] >= intervals[i][0]:
            res[-1][1] = max(intervals[i][1], res[-1][1])
        else:
            res.append(intervals[i])
    
    return res
        
# Time Complexity = O(n * log n)
# Space Complexity = O(1) (result array does not count as auxiliary space) 
# OR
# Space Complexity = O(logn)/O(n) in case we take into consideration the sorting and type of sorting used