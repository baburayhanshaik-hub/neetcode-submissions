class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        temp = [0 for _ in range(n)]
        for i in range(n):
            for j in range(i+1):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i] = matrix[i][::-1]