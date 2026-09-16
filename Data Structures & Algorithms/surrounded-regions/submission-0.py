class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        def dfs(x,y):
            if ( (x,y) in visited or
                 not (0<=x<len(board) and 0<=y<len(board[0])) or
                 board[x][y]=="X"
                ):
                return
            visited.add((x,y))
            for i,j in [[-1,0],[1,0],[0,-1],[0,1]]:
                dfs(x+i,y+j)
        for i in range(len(board)):
            if board[i][0]=="O":
                dfs(i,0)
            if board[i][len(board[0])-1]=="O":
                dfs(i,len(board[0])-1)
        
        for i in range(len(board[0])):
            if board[0][i]=="O":
                dfs(0,i)
            if board[len(board)-1][i]=="O":
                dfs(len(board)-1,i)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in visited:
                    board[i][j]="X"