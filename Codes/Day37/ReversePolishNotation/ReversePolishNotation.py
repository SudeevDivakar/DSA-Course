def rev_pol_not(tokens):
    stack = []
    #write your code here
    for i in tokens:
        if i in '+-*/':
            num2 = stack.pop()
            num1 = stack.pop()
            if i == '+':
                stack.append(num1 + num2)
            elif i == '-':
                stack.append(num1 - num2)
            elif i == '*':
                stack.append(num1 * num2)
            else:
                stack.append(int(num1 / num2))   # Do not use // because truncating != floor division
        else:
            stack.append(int(i))
    
    return stack.pop()


# Time Complexity = O(n)
# Space Complexity = O(n)