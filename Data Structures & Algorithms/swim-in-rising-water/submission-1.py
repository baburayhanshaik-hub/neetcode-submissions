import heapq
class Solution:
    def swimInWater(self, grid):        
        heap = [[0,0,0]]
        ans = {}

        def checkmax(m,n):
            res = grid[m][n]
            while ans[(m,n)][1]!=None:
                m,n = ans[(m,n)][1]
                res = max(res,grid[m][n])
            return res
        dummy =[[float("inf") for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans[(i,j)] = [float("inf"),None]
        ans[(0,0)] = [0,None]
        dummy[0][0] = 0
        visited = set()
        n = 0
        while heap:
            w,i,j = heapq.heappop(heap)
            visited.add((i,j))
            for r,c in [[-1,0],[1,0],[0,1],[0,-1]]:
                if 0<=r+i<len(grid) and 0<=c+j<len(grid[0]) and (r+i,c+j) not in visited:
                    if dummy[r+i][c+j]>grid[r+i][c+j]:
                        ans[(r+i,c+j)] = [grid[r+i][c+j],(i,j)]
                        heapq.heappush(heap,[grid[r+i][c+j],r+i,c+j])
                        dummy[r+i][c+j] = max(grid[r+i][c+j],grid[i][j])
        return checkmax(len(grid)-1,len(grid[0])-1)