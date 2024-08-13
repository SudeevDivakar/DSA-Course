def solveSudoku(board):
    #The function modifies the board in place to present the solution .Hence there is no need to return the board
    
    hashTable = {
        0: 0,
        1: 0,
        2: 0,
        3: 3,
        4: 3,
        5: 3,
        6: 6,
        7: 6,
        8: 6
    }
    
    def isValid(i, j, k):
        if k not in board[i]:
            for row in board:
                if k == row[j]:
                    return False
            else:
                for row in range(hashTable[i], hashTable[i] + 3):
                    if k in board[row][hashTable[j]: hashTable[j] + 3]:
                        return False
                else:
                    return True
        else:
            return False
                        
        
    
    def fillBoard(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if isValid(i, j, num):
                            board[i][j] = num
                            if fillBoard(board):
                                return True
                            board[i][j] = '.'
                    else:
                        return False
                            
        
        return True
        

    fillBoard(board)
    
    return board

print(solveSudoku([
["5", "3", ".", ".", "7", ".", ".", ".", "."],
["6", ".", ".", "1", "9", "5", ".", ".", "."],
[".", "9", "8", ".", ".", ".", ".", "6", "."],
["8", ".", ".", ".", "6", ".", ".", ".", "3"],
["4", ".", ".", "8", ".", "3", ".", ".", "1"],
["7", ".", ".", ".", "2", ".", ".", ".", "6"],
[".", "6", ".", ".", ".", ".", "2", "8", "."],
[".", ".", ".", "4", "1", "9", ".", ".", "5"],
[".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))

# Time Complexity = O(1)
# Space Complexity = O(1)