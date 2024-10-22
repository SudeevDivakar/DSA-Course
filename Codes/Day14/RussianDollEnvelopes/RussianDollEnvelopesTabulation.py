def maxEnvelopes(envelopes):
    #Write code here
    envelopes.sort()
    n = len(envelopes)
    
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                
    return max(dp)

# Time Complexity = O(n ^ 2)
# Space Complexity = O(n)