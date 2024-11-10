# Define the adjacency list of the graph
adjacency_list = {
    'A': ['B', 'F'],
    'B': ['A', 'C'],
    'C': ['B', 'E', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'C', 'F'],
    'F': ['A', 'E']
}
 
# Recursive function for Depth-first search (DFS)
def trav_recursive_DFS(graph, vertex, output, visited):
    output.append(vertex)
    visited.add(vertex)

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            trav_recursive_DFS(graph, neighbour, output, visited)
    
    return output

print(trav_recursive_DFS(adjacency_list, 'A', [], set()))


# Time Complexity = O(V + E)
# Space Complexity = O(V)