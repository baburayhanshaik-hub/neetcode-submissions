class TrieNode:
    def __init__(self):
        self.dic = {}
        self.end = False
    def addword(self,word):
        curr = self
        for i in word:
            if i not in curr.dic:
                curr.dic[i] = TrieNode()
            curr = curr.dic[i]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        node = TrieNode()
        for i in words:
            node.addword(i)

        res, visited = set(), set()
        row, col = len(board), len(board[0])
        def func(x,y,curr,word):
            if ( x<0 or y<0 or x==len(board)
                 or y == len(board[0]) or (x,y) in visited
                 or board[x][y] not in curr.dic
                ):
                if curr.end==True:
                    res.add(word)
                return

            if curr.end==True:
                res.add(word)
            visited.add((x,y))
            func(x+1,y,curr.dic.get(board[x][y]),word+board[x][y])
            func(x-1,y,curr.dic.get(board[x][y]),word+board[x][y])
            func(x,y+1,curr.dic.get(board[x][y]),word+board[x][y])
            func(x,y-1,curr.dic.get(board[x][y]),word+board[x][y])
            visited.remove((x,y))
        for i in range(row):
            for j in range(col):
                func(i,j,node,"")
        return list(res)












