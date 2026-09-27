class Solution:
    def climbStairs(self, n: int) -> int:
        visited = {0:1,-1:0}
        def func(n):
            if n in visited:
                return visited[n]
            ans = func(n-1)+func(n-2)
            visited[n] = ans
            return ans
        return func(n)