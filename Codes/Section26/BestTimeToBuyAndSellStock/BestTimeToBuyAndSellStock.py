def maxProfit(prices):
    #write code here
    left = 0
    right = 1
    
    max_profit = 0
    
    while right < len(prices):
        if prices[right] >= prices[left]:
            if prices[right] - prices[left] > max_profit:
                max_profit = prices[right] - prices[left]
            right += 1
        else:
            left += 1

    return max_profit


# Time Complexity = O(n)
# Space Complexity = O(1)