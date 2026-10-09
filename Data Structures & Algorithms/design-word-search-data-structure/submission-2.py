class Trie:
    def __init__(self):
        self.dic = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.dic = Trie()
        
    def addWord(self, word: str) -> None:
        curr = self.dic
        for i in word:
            if i not in curr.dic:
                curr.dic[i] = Trie()
            curr = curr.dic[i]
        curr.end=True

    def search(self, word: str) -> bool:
        curr = self.dic
        def func(x,curr,prev):
            if x>=len(word):
                if word[x-1]=="." and curr.end==True:
                    return True
                return False
            for i in range(x,len(word)):
                if word[i]==".":
                    for ch in curr.dic.keys():
                        if func(i+1,curr.dic[ch],curr):
                            return True
                    return False 
                if word[i] not in curr.dic:
                    curr.dic[word[i]] = Trie()
                curr = curr.dic[word[i]]
            if curr.end==True:
                return True
            return False
        return func(0,curr,curr)