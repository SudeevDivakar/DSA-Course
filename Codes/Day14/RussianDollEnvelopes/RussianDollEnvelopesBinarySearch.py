def bin_search(temp, num):
    left, right = 0, len(temp) - 1
    
    while left < right:
        mid = (left + right) // 2
        if num > temp[mid]:
            left = mid + 1
        else:
            right = mid
    
    return left

def maxEnvelopes(envelopes):
    #Write code here
    envelopes.sort(key = lambda x:(x[0], -x[1]))
    n = len(envelopes)
    temp = [envelopes[0][1]]
    
    for i in range(1, n):
        if envelopes[i][1] > temp[-1]:
            temp.append(envelopes[i][1])
        else:
            ind = bin_search(temp, envelopes[i][1])
            temp[ind] = envelopes[i][1]
    
    return len(temp)

# Time Complexity = O(n * log n)
# Space Complexity = O(n)