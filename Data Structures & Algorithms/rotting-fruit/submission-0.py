class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    rotten.append([i,j])
        ans = 0
        while rotten:
            x,y = rotten.pop(0)
            for i,j in [[0,1],[0,-1],[1,0],[-1,0]]:
                if 0<=i+x<len(grid) and 0<=j+y<len(grid[0]):
                    if grid[i+x][j+y]==1:
                        grid[i+x][j+y]=1+grid[x][y]
                        ans = max(ans, grid[i+x][j+y])
                        rotten.append([i+x,j+y])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return 0 if ans-2<0 else ans-2