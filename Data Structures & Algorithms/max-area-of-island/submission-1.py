class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        track = [[0 for i in range(m)] for j in range(n)]
        res=0
        def func(i,j):
            nonlocal res
            track[i][j]=1
            res+=1
            for i1,j1 in [[0,1],[0,-1],[1,0],[-1,0]]:
                if 0<=i+i1<n and 0<=j+j1<m and grid[i+i1][j+j1]==1 and track[i+i1][j+j1]==0:
                    func(i+i1,j+j1)
        
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and track[i][j]==0:
                    func(i,j)
                max_area = max(res, max_area)
                res=0
        
        return max_area