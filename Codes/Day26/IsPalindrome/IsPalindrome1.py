# Create New String (Not Optimal)

def is_palindrome(str):
    new_str = ''

    for i in reversed(range(len(str))):
        new_str += str[i]

    if str == new_str:
        return True
    
    return False

# Time Complexity = O(n ^ 2) because appending onto strings is a O(n) task (Strings are immutable in python, js, etc)
# Space Complexity = O(n)