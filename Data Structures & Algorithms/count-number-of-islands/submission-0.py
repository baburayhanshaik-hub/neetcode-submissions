class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        track = [["0" for i in range(m)] for j in range(n)]
        def func(i,j):
            track[i][j] = "1"
            for i1, j1 in [[-1,0],[0,1],[1,0],[0,-1]]:
                if 0<=i+i1<n and 0<=j+j1<m and grid[i+i1][j+j1]=="1" and track[i+i1][j+j1]=="0":
                    func(i+i1,j+j1)
        
        for i in range(n):
            for j in range(m):
                print(track)
                if track[i][j]=="0" and grid[i][j]=="1":
                    ans+=1
                    func(i,j)
        return ans