from collections import deque

def validPath(n, edges, source, destination):
    # Create the graph as an adjacency list
    graph = [[] for _ in range(n)]
    
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    #write code here
    visited = set()
    queue = deque([source])
    
    while len(queue) > 0:
        node = queue.popleft()
        visited.add(node)
        if node == destination:
            return True
        
        for i in graph[node]:
            if i not in visited:
                queue.append(i)
    
    return False
