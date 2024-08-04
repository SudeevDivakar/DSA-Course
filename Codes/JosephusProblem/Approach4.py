# Same ideology as recursive method 2 but using iteration

def findTheWinner(n, k):
    pos = 0
    for i in range(2,n+1):
        pos = (pos + k) % i
    pos += 1 
    return pos
        

#Time Complexity = O(n)
#Space Complexity = O(1)