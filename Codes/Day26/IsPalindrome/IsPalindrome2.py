# Create New Array

def is_palindrome(str):
    new_array = []

    for i in reversed(range(len(str))):
        new_array.append(str[i])

    if ''.join(new_array) == str:
        return True
    
    return False

# Time Complexity = O(n)
# Space Complexity = O(n)