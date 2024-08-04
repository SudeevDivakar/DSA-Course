# Recursive method number 2
# We can use the result of n-1 people standing in a circle to determine the result of n people standing in a circle


def findTheWinner(n, k):
    #write code here
    arr = list(range(n))
    def helper(n, k):
        if n == 1:
            return 0
        else:
            return (helper(n-1, k) + k) % n
            
    return helper(n, k) + 1


# Time Complexity = O(n) because no manipulating array
# Space Complexity = O(n) depth of recursive call stack