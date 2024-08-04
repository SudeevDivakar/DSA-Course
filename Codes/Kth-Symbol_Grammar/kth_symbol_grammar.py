def kth_symbol(n, k):
    #write your code here
    global complement
    if n == 1:
        return 0
    else:
        last_row_len = 2 ** (n-1)
        mid = last_row_len // 2
        if k > mid:
            return int(not(kth_symbol(n - 1, k - mid)))
        else:
            return kth_symbol(n - 1, k)
    
