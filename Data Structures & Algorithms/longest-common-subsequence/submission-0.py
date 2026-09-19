class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n  = len(text1)+1,len(text2)+1
        grid = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                i1,j1 = i-1,j-1
                if text1[i1]==text2[j1]:
                    grid[i][j]=1+grid[i-1][j-1]
                else:
                    grid[i][j]=max(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]