def findMinArrowShots(points):
    #write code here
    if len(points) == 0:
        return 0
        
    points.sort(key=lambda x: x[1])
    
    res = 1
    end = points[0][1]
    for i in range(1, len(points)):
        if points[i][0] > end:
            res += 1
            end = points[i][1]
            
    return res
    
# Time Complexity = O(n * log n)
# Space Complexity = O(n) / O(log n)  ->  based on sorting algorithm used