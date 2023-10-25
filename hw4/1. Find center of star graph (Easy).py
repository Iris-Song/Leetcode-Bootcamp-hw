class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)+1
        indegree = [0]*(n+1)

        for u,v in edges:
            indegree[u]+=1
            indegree[v]+=1
        for i in range(n+1):
            if indegree[i]>1:
                return i
            