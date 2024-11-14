from collections import deque

def numIslands(grid):
    #write code here
    if len(grid) == 0:
        return 0
    
    m, n = len(grid), len(grid[0])

    def DFS(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        else:
            grid[i][j] = '0'
            DFS(i + 1, j)
            DFS(i, j + 1)
            DFS(i - 1, j)
            DFS(i, j - 1)
                        
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                res += 1
                DFS(i, j)
                
    return res