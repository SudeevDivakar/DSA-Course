from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]

        for i in prerequisites:
            graph[i[1]].append(i[0])

        def checkCycleBFS(graph, node):
            queue = deque()
            visited = set()
            for i in graph[node]:
                queue.append(i)
            while len(queue) > 0:
                curr = queue.popleft()
                visited.add(curr)
                if curr == node:
                    return True

                for neighbour in graph[curr]:
                    if neighbour not in visited:
                        queue.append(neighbour)

            return False
                 
        for i in range(numCourses):
            if checkCycleBFS(graph, i):
                return False
        
        return True

# Time Complexity = O(p + (n ^ 2) + (n * E))   where p => length of prerequisites array, n => number of vertices, E => number of edges
# Space Complexity = O(n + E)   where n => number of vertices, E => number of edges