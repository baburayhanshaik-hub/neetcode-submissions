class Solution:
    def isHappy(self, n: int) -> bool:
        res = 0
        visited = {n}
        while True:
            if n == 1:
                return True
            while n:
                res+=(n%10)**2
                n=n//10
            n = res
            if res in visited:
                return False
            res = 0
            visited.add(n)