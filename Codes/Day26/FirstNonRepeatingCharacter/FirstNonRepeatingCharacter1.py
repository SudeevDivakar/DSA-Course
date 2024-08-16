# Brute Force

def non_repeating_char(str):
    for i in range(len(str)):
        repeat = False
        for j in range(len(str)):
            if i != j and str[i] == str[j]:
                repeat = True
        if repeat == False:
            return i
    
    return None

# Time Complexity = O(n ^ 2)
# Space Complexity = O(1)