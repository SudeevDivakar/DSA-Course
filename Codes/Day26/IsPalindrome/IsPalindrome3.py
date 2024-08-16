# Two Pointer Solution

def is_palindrome(str):
    #write code here
    
    start, end = 0, len(str) - 1
    while(start <= end):
        if str[start] != str[end]:
            return False
        else:
            start += 1
            end -= 1
            
    return True

# Time Complexity = O(n)
# Space Complexity = O(1)