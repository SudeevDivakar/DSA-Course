# Intuitive approach (deleting elements from the array recursive)

def findTheWinner(n, k):
    #write code here
    array = list(range(1,n+1))
    def helper(arr, start):
        if(len(arr) == 1):
            return arr[0]
        else:
            start += (k-1) % len(arr)
            if(start >= len(arr)):
                start %= len(arr)
            arr.pop(start)
            return helper(arr, start)

    return helper(array, 0)

# Time Complexity = O(n^2) because time complexity of removing an element from an array is O(n)
# Space Complexity = O(n)