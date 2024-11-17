def eraseOverlapIntervals(intervals):
    #write code here
    if len(intervals) == 0:
        return 0
        
    intervals.sort()
    
    res = 0
    prev_end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < prev_end:
            prev_end = min(prev_end, intervals[i][1]) 
            res += 1
        else:
            prev_end = intervals[i][1]
    
    return res

# Time Complexity = O(n * log n)
# Space Complexity = O(n) / O(log n)     depending on sorting algorithm used