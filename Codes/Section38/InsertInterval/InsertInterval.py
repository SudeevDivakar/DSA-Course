def insert(intervals, newInterval):
    #write code here
    n = len(intervals)
    res = []
    
    for i in range(n):
        if intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
        
        elif intervals[i][0] > newInterval[1]:
            res.append(newInterval)
            res.extend(intervals[i:])            
            break
        
        else:
            start = min(newInterval[0], intervals[i][0])
            end = max(newInterval[1], intervals[i][1])
            newInterval[0] = start
            newInterval[1] = end
    else:
        res.append(newInterval)
            
    return res


# Time Complexity = O(n)
# Space Complexity = O(1) (Assuming output array does not count as auxiliary space)