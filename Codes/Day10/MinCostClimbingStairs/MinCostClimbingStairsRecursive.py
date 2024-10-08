def minCostClimbingStairs(cost):
    n = len(cost)
    #write code here
    def costFrom(i):
        if i > n - 1:
            return 0
            
        return cost[i] + min(costFrom(i + 1), costFrom(i + 2))
    
    return min(costFrom(0), costFrom(1))

# Time Complexity = O(2 ^ n)
# Space Complexity = O(n) - Space used by recursive call stack