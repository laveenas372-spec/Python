class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def dfs(v,res):
            if v in visit:
                return 
            visit.add(v)
            res.append(v)
            for nei in adj[v]:
                dfs(nei,res)
            


        adj = defaultdict(list)
        for v1,v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        
        visit = set()    
        res = 0

        for v in range(n):
            if v in visit:
                continue

            component = []
            dfs(v,component)

            if all(
                len(component) - 1 == len(adj[node]) 
                for node in component
                ):

                res +=1
            
    
        return res