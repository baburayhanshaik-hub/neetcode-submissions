class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        block = defaultdict(list)
        row = defaultdict(list)
        col = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] in block[(i//3,j//3)]:
                    print("hehe")
                    return False
                elif board[i][j] in row[i]:
                    print("haha",i)
                    return False
                elif board[i][j] in col[j]:
                    print("huhu")
                    return False
                if board[i][j]!=".":
                    block[(i//3,j//3)].append(board[i][j])
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
        return True