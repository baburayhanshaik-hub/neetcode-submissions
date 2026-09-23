class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        visited = {}
        def func(i,j):
            if (i,j) in visited:
                return visited[(i,j)]
            if i>=len(s) and j>=len(p):
                return True
            elif j>=len(p):
                return False
            if j<len(p)-1 and p[j+1]=="*":
                ans = (i<len(s) and (s[i]==p[j] or p[j]==".") and func(i+1,j)) or func(i,j+2)
            else:
                ans = (i<len(s) and (s[i]==p[j] or p[j]==".") and func(i+1,j+1))
            visited[(i,j)] = ans
            return ans
        return func(0,0)