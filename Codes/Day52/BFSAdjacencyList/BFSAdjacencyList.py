from collections import deque

adjacency_list = {
    'A': ['B', 'F'],
    'B': ['A', 'F', 'C'],
    'C': ['B', 'E', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'C', 'F'],
    'F': ['A', 'B', 'E']
}

def BFSAdjacencyList(graph, start):
    visited = {start}
    queue = deque([start])

    output = []

    while len(queue) > 0:
        element = queue.popleft()
        output.append(element)
        for i in graph[element]:
            if i not in visited:
                queue.append(i)
                visited.add(i)
    
    return output

print(BFSAdjacencyList(adjacency_list, 'A'))
        
# Time Complexity = O(V + E) where V => number of vertices and E => number of edges
# Space Complexity = O(V)