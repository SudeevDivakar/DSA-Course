def numTrees(n):
    #write code here 
    dp = {}
    
    def helper(left, right):
        if left > right:
            return 1
        
        if (left, right) in dp:
            return dp[(left, right)]
            
        res = 0
        
        for val in range(left, right + 1):
            left_count = helper(left, val - 1)
            right_count = helper(val + 1, right)
            res += left_count * right_count
        
        dp[(left, right)] = res
        return dp[(left, right)]
            
    return helper(1, n)