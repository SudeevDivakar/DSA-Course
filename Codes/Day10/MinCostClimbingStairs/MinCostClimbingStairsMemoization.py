def minCostClimbingStairs(cost):
    n = len(cost)
    ht = {}
    #write code here
    def costFrom(i):
        if i > n - 1:
            return 0
            
        if i + 1 not in ht:
            ht[i + 1] = costFrom(i + 1)
        if i + 2 not in ht:
            ht[i + 2] = costFrom(i + 2)
        return cost[i] + min(ht[i + 1], ht[i + 2])
    
    return min(costFrom(0), costFrom(1))

# Time Complexity = O(n)
# Space Complexity = O(n) - Space used by recursive call stack and hashmap/array