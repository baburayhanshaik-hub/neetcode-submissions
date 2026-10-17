class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = {}
        if n<0:
            n*=-1
            x = 1/x
        def func(x,n):
            if n in ans:
                return ans[n]
            if n==0:
                return 1
            if n==1:
                return x
            if n%2==0:
                res = func(x,n//2)*func(x,n//2)
            else:
                res = x*func(x,n//2)*func(x,n//2)
            ans[n] = res
            return res
        return func(x,n)