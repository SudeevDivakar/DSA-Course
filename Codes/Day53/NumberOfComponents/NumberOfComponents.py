def build_adj_list(n, edges):
    graph = {}

    for i in edges:
        vertex1 = i[0]
        vertex2 = i[1]

        if vertex1 not in graph:
            graph[vertex1] = [vertex2]
        else:
            graph[vertex1].append(vertex2)
        
        if vertex2 not in graph:
            graph[vertex2] = [vertex1]
        else:
            graph[vertex2].append(vertex1)
        
    for i in range(n):
        if i not in graph:
            graph[i] = []
    
    return graph

def DFS(graph, vertex, visited):
    visited.add(vertex)

    for i in graph[vertex]:
        if i not in visited:
            DFS(graph, i, visited)

def count_components(n, edges):
    graph = build_adj_list(n, edges)

    visited = set()

    count = 0
    for i in range(n):
        if i not in visited:
            DFS(graph, i, visited)
            count += 1
    
    return count

n = 7  # vertices 0, 1, 2, 3, 4, 5, 6
edges = [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6]]
print(count_components(n, edges))


# Time Complexity = O(V + E)
# Space Complexity = O(V + E)