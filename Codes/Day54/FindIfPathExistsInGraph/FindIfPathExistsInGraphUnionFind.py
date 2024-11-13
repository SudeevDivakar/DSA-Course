class Solution:
    def validPath(self, n, edges, source, destination):
        rank = [1] * n
        par = [i for i in range(n)]

        def find(n):
            res = n

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            
            return res
        
        def union(n1, n2):
            n1, n2 = find(n1), find(n2)

            if n1 == n2:
                return

            if rank[n1] > rank[n2]:
                par[n2] = n1
                rank[n1] += rank[n2]
            else:
                par[n1] = n2
                rank[n2] += rank[n1]

        for i in edges:
            union(i[0], i[1])
        
        if find(source) == find(destination):
            return True
            
        else:
            return False