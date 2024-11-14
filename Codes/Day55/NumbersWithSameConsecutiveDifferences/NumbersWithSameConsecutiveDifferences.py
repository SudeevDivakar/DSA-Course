def numsSameConsecDiff(n, k):
    #write code here
    if n == 1:
        return [i for i in range(10)]
        
    def helper(num, n, k, res):
        if n == 0:
            res.append(num)
            return
        
        last_digit = num % 10
        
        if k == 0:
            helper((num * 10) + (last_digit), n - 1, k, res)
            return
        
        if last_digit + k < 10:
            helper((num * 10) + (last_digit + k), n - 1, k, res)
            
        if last_digit - k >= 0:
            helper((num * 10) + (last_digit - k), n - 1, k, res)
        
    
    res = []
    for i in range(1, 10):
        helper(i, n - 1, k, res)
    
    return res