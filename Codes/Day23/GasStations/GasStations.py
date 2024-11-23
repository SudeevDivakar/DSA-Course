def canCompleteCircuit(gas, cost):
    #write code here
    if sum(gas) < sum(cost):
        return -1
    
    total = 0
    res = 0
    
    for i in range(len(gas)):
        total += (gas[i] - cost[i])
        
        if total < 0:
            total = 0
            res = i + 1
            
    return res

# Time Complexity = O(n)
# Space Complexity = O(1)