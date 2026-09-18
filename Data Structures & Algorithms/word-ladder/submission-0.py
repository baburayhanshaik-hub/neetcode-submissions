from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = defaultdict(list)
        for i in wordList:
            for j in range(len(i)):
                word = i[:j]+"*"+i[j+1:]
                adj[word].append(i)
        queue = [[beginWord,1]]
        visited = set()
        while queue:
            word,pos = queue.pop(0)
            if word == endWord:
                return pos
            for i in range(len(word)):
                x = word[:i]+"*"+word[i+1:]
                for j in adj[x]:
                    if j not in visited:
                        queue.append([j,pos+1])
                    visited.add(j)
            adj[x]=[]
        print(pos)
        return 0