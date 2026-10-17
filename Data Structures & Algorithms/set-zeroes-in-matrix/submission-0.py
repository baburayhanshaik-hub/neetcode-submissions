class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n,m = len(matrix),len(matrix[0])
        track = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    track.append([i,j])
        
        for i,j in track:
            for c in range(len(matrix)):
                matrix[c][j]=0
            for r in range(len(matrix[0])):
                matrix[i][r]=0