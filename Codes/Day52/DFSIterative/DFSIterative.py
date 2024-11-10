# Define the adjacency list of the graph
adjacency_list = {
    'A': ['B', 'F'],
    'B': ['A', 'F', 'C'],
    'C': ['B', 'E', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'C', 'F'],
    'F': ['A', 'B', 'E']
}
 
# Iterative function for Depth-first search (DFS)
def trav_DFS_iterative(graph, start):
    output = []
    stack = [start]
    visited = {start}

    while len(stack) > 0:
        vertex = stack.pop()
        output.append(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)
        
    return output

print(trav_DFS_iterative(adjacency_list, 'A'))