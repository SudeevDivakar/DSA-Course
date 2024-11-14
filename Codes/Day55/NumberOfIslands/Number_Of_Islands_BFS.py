from collections import deque

def numIslands(grid):
    #write code here
    if len(grid) == 0:
        return 0
    
    m, n = len(grid), len(grid[0])
    visited = set()
    
    def BFS(i, j):
        queue = deque([(i, j)])
        visited.add((i, j))
        
        while len(queue) > 0:
            x, y = queue.popleft()
            
            destinations = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            
            for dr, dc in destinations:
                fx = dr + x
                fy = dc + y
                if (fx >= 0 and fx < m) and (fy >= 0 and fy < n) \
                    and grid[fx][fy] == '1' and (fx, fy) not in visited:
                        queue.append((fx, fy))
                        visited.add((fx, fy))
                        
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and (i, j) not in visited:
                res += 1
                BFS(i, j)
                
    return res