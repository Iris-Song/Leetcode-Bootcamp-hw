class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        g = collections.defaultdict(list)

        for i,j in prerequisites:
            indegree[i]+=1
            g[j].append(i)
        
        q = []
        vis = set()
        for i,d in enumerate(indegree):
            if d==0:
                q.append(i)
                vis.add(i)
        
        while q:
            node = q.pop()
            for nxt in g[node]:
                indegree[nxt]-=1
                if nxt not in vis and indegree[nxt]<=0:
                    vis.add(nxt)
                    q.append(nxt)
        
        return len(vis)==numCourses