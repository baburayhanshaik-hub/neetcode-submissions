class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        visited = {}
        def asc(x,y,prev):
            if not((0<=x<len(matrix) and 0<=y<len(matrix[0]))):
                return 0
            if matrix[x][y]<=prev:
                return 0
            if (x,y) in visited:
                return visited[(x,y)]
            ans = 0
            for i,j in [[-1,0],[1,0],[0,-1],[0,1]]:
                ans = max(ans, 1+asc(x+i,y+j,matrix[x][y]))
            visited[(x,y)]=ans
            return visited[(x,y)]
        def func():
            res = 0
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if (i,j) not in visited:
                        res = max(res,asc(i,j,float("-inf")))
            return res
        ans = func()
        print(visited, ans)
        return ans