import copy

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[0 for i in range(len(board[0]))] for i in range(len(board))]
        ans = 0
        def func(vis,l,r,n):
            nonlocal ans
            if n+1>=len(word):
                ans = 1
            for i,j in [[-1,0],[1,0],[0,-1],[0,1]]:
                if ans == 0 and (0<=i+l<len(vis) and 0<=j+r<len(vis[0])) and vis[i+l][j+r]==0:
                    if board[i+l][j+r]==word[n+1]:
                        vis[i+l][j+r]=1
                        func(vis,i+l,r+j,n+1)
                        vis[i+l][j+r]=0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    visited[i][j]=1
                    func(visited,i,j,0)
                    visited[i][j]=0
            if ans == 1:
                break
        return ans==1