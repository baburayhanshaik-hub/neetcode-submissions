from typing import List

class TrieNode:
    def __init__(self):
        self.dic = {}
        self.word = None

    def addword(self, word):
        curr = self
        for ch in word:
            if ch not in curr.dic:
                curr.dic[ch] = TrieNode()
            curr = curr.dic[ch]
        curr.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []

        root = TrieNode()
        for word in words:
            root.addword(word)

        row, col = len(board), len(board[0])
        res = []

        def dfs(x, y, parent):
            ch = board[x][y]
            node = parent.dic.get(ch)

            if node is None:
                return

            # Found a complete word
            if node.word is not None:
                res.append(node.word)
                node.word = None  # Prevent duplicate results

            # Mark the cell as visited
            board[x][y] = "#"

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy

                if (0 <= nx < row and 0 <= ny < col
                        and board[nx][ny] != "#"):
                    dfs(nx, ny, node)

            # Restore the original cell
            board[x][y] = ch

            # Prune exhausted Trie branches
            if not node.dic and node.word is None:
                del parent.dic[ch]

        for i in range(row):
            for j in range(col):
                dfs(i, j, root)

        return res