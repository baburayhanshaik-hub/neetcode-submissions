class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n,m = len(matrix),len(matrix[0])
        i_vis = set()
        j_vis = set()
        track = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    track.append([i,j])
        
        for i,j in track:
            if j not in j_vis:
                for c in range(len(matrix)):
                    matrix[c][j]=0
                j_vis.add(j)
            if i not in i_vis:
                for r in range(len(matrix[0])):
                    matrix[i][r]=0
                i_vis.add(i)