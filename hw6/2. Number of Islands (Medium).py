class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i,j):
            if(grid[i][j]!='1'):
                return
            grid[i][j] = '#'
            for di,dj in dirs:
                newi = i+di
                newj = j+dj
                if 0<=newi<m and 0<=newj<n:
                    dfs(newi,newj)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    dfs(i,j)
                    res+=1
        
        return res