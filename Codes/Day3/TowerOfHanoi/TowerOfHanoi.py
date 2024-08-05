def toh(N, fromm, to, aux):
    #code below
    # sample print statement below
    #print("move disk " + 1 + " from rod " + 1 + " to rod " + 2)
    #in the above statement consider we are moving disk 1 from rod 1 to rod 2
    #remember to return number of moves as well
    c = 0
    def helper(N, fromm, to, aux):
        nonlocal c
        if N == 1:
            print(f'move disk {N} from rod {fromm} to rod {to}')
            c += 1
        else:
            helper(N-1, fromm, aux, to)
            print(f'move disk {N} from rod {fromm} to rod {to}')
            c += 1
            helper(N-1, aux, to, fromm)

    helper(N, fromm, to, aux)
    return c
    
print(toh(5,1,3,2))


# Space Complexity = O(n) (Depth of recursive call stack)
# Time Complexity = O(2^n) 