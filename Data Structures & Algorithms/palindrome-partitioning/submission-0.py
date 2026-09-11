class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        res = []
        def func(n):
            if n>=len(s):
                res.append(ans.copy())
                return
            for i in range(n,len(s)):
                if s[n:i+1]==s[n:i+1][::-1]:
                    ans.append(s[n:i+1])
                    func(i+1)
                    ans.pop()
        func(0)
        return res