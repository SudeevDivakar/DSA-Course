# Intuitive approach (deleting elements from the array iterative)

def findTheWinner(n, k):
    #write code here
    arr = list(range(1, n+1))
    i = 0
    while(len(arr) != 1):
        i += (k-1) % len(arr)
        if(i >= len(arr)):
            i %= len(arr)
        arr.pop(i)
    return arr[0]

# Time Complexity = O(n^2) because time complexity of removing an element from an array is O(n)
# Space Complexity = O(n)