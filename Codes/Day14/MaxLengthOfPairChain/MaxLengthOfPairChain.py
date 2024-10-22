def findLongestChain(pairs):
    #Write code here
    pairs.sort()
    n = len(pairs)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if pairs[i][0] > pairs[j][1] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                
    return max(dp)

# Time Complexity = O(n ^ 2)
# Space Complexity = O(n)