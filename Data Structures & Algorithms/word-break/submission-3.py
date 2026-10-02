class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        visited = {}
        def func(x,res):
            if x in visited:
                return visited[x]
            if x>=len(s):
                return True
            for i in range(x,len(s)):
                res+=s[i]
                if res in wordDict:
                    if func(i+1,""):
                        visited[x] = True
                        return True
            visited[x] = False
            return False
        return func(0,"")