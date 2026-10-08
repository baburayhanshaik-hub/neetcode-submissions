class Trie:
    def __init__(self):
        self.node = {}
        self.end = False

class PrefixTree:
    def __init__(self):
        self.trie = Trie()

    def insert(self, word: str) -> None:
        curr = self.trie
        for i in word:
            if i not in curr.node:
                curr.node[i] = Trie()
            curr = curr.node[i]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.trie
        for i in word:
            if i not in curr.node:
                return False
            curr = curr.node[i]
        if curr.end == True:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for i in prefix:
            if i not in curr.node:
                return False
            curr = curr.node[i]
        return True