def fractionalknapsack(W,arr,n):
    #write code here
    arr.sort(key=lambda x: x[0] / x[1])
    
    res = 0
    i = len(arr) - 1
    while W > 0 and i > -1:
        item = arr[i]
        
        if W - item[1] > 0:
            res += item[0]
            W -= item[1]
        else:
            amount = (W * item[0]) / item[1]
            res += amount
            W = 0
        
        i -= 1
            
    return res

# Time Complexity = O(n * log n)
# Space Complexity = O(1)    not considering space used for sorting