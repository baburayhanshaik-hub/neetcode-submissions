class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        zeros = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    zeros.append([i,j])
        print(zeros)
        while zeros:
            x,y = zeros.pop(0)
            for i,j in [[0,1],[0,-1],[-1,0],[1,0]]:
                if 0<=i+x<len(grid) and 0<=j+y<len(grid[0]):
                    if grid[i+x][j+y]==2147483647:
                        grid[i+x][j+y]=1+grid[x][y]
                        zeros.append([i+x,j+y])
            













