class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        pas, atl = set(), set()
        row, col = len(grid), len(grid[0])
        def dfs(row, col, visit, height):
            if ((row,col) in visit or
                not (0<=row<len(grid) and 0<=col<len(grid[0])) or
                grid[row][col]<height
                ):
                return
            visit.add((row,col))
            height = grid[row][col]
            dfs(row-1, col, visit, height)
            dfs(row+1, col, visit, height)
            dfs(row, col+1, visit, height)
            dfs(row, col-1, visit, height)

        for c in range(col):
            dfs(0,    c,pas, grid[0][c])
            dfs(row-1,c,atl, grid[row-1][c])
        
        for r in range(row):
            dfs(r, 0 , pas, grid[r][0])
            dfs(r, col-1, atl, grid[r][col-1])

        res = []
        for i in range(row):
            for j in range(col):
                if (i,j) in pas and (i,j) in atl:
                    res.append([i,j])
        return res