class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for i in prerequisites:
            graph[i[1]].append(i[0])
            indegree[i[0]] += 1

        count = 0
        stack = []

        for i in range(len(indegree)):
            if indegree[i] == 0:
                stack.append(i)
        
        while len(stack) > 0:
            node = stack.pop()
            count += 1
            for i in graph[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    stack.append(i)
            
        if count == numCourses:
            return True
        else:
            return False
        
# Time Complexity = O(p + n + E)    where p => length of prerequisites array, n => number of vertices, E => number of edges
# Space Complexity = O(n + E)    where n => number of vertices, E => number of edges