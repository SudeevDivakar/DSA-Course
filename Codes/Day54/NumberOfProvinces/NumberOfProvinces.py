def findCircleNum(isConnected):
    #write code here
    visited = set()
    
    def DFS(isConnected, node, visited):
        visited.add(node)
        
        for i in range(len(isConnected[node])):
            if isConnected[node][i] == 1:
                if i not in visited:
                    DFS(isConnected, i, visited)
        
    count = 0
    for i in range(len(isConnected)):
        if i not in visited:
            DFS(isConnected, i, visited)
            count += 1
    
    return count

# Time Complexity = O(n ^ 2)
# Space Complexity = O(n)