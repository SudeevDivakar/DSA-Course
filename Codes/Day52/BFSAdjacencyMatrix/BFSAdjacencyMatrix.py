from collections import deque

vertices = ['A', 'B', 'C', 'D', 'E', 'F']
vertex_indices = { 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5 }
 
# The adjacency matrix
adjacency_matrix = [
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 0]
]

def BFSAdjacencyMatrix(graph, start):
    queue = deque([start])
    output = []
    visited = {start}

    while len(queue) > 0:
        element = queue.popleft()
        output.append(element)
        idx = vertex_indices[element]

        for i in range(len(graph[idx])):
            if graph[idx][i] == 1 and vertices[i] not in visited:
                queue.append(vertices[i])
                visited.add(vertices[i])

    return output

print(BFSAdjacencyMatrix(adjacency_matrix, 'A'))

# Time Complexity = O(V ^ 2)
# Space Complexity = O(V)