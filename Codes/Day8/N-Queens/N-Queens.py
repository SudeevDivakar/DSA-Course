def solveNQueens(n):
    #write code here
    
    solutions = []
    subset = ['.' * n] * n
    
    def isValid(i, j, board):
        for row in range(i):
            if board[row][j] == 'Q':
                return False
        count = 1
        while i - count >= 0:
            if j - count >= 0 and board[i - count][j - count] == 'Q':
                return False
            if j + count < n and board[i - count][j + count] == 'Q':
                return False
                
            count += 1
            
        return True
                

    def helper(i):
        if i == n:
            solutions.append(list(subset))
        
        else:
            for j in range(n):
                if isValid(i, j, subset):
                    subset[i] = '.' * j + 'Q' + '.' * (n-(j+1))
                    helper(i + 1)
                    subset[i] = '.' * n
    
    helper(0)
    
    return solutions
    
print(solveNQueens(4))

# Time Complexity = O(n!)
# Space Complexity = O(n ^ 2)