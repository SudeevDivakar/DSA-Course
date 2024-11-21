def twoCitySchedCost(costs):
    #write code here
    n = len(costs)
    costs.sort(key=lambda x: x[0] - x[1])
    
    res = 0
    for i in range(n):
        if i < n / 2:
            res += costs[i][0]
        else:
            res += costs[i][1]
    
    return res

# Time Complexity = O(n * log n)
# Space Complexity = O(n) / O(log n)   -> based on sorting algorithm used