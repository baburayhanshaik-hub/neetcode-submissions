class Solution:
    def numDecodings(self, s: str) -> int:
        visited = {}
        def func(i):
            if i in visited:
                return visited[i]
            if i>=len(s):
                return 1
            if s[i]=="0":
                return 0
            ans = func(i+1)
            if i+2<=len(s) and s[i:i+2]<="26":
                ans+=func(i+2)
            visited[i] = ans
            return ans
        return func(0)