class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def func(x, y):
            if y == len(t):
                return 1
            if x == len(s):
                return 0
            if (x, y) in memo:
                return memo[(x, y)]
                
            ans = func(x + 1, y)
            if s[x] == t[y]:
                ans+= func(x + 1, y + 1)
            
            memo[(x, y)] = ans
            return ans

        return func(0, 0)