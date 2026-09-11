class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def func(l,r,res):
            nonlocal ans
            if l==0 and r==0:
                ans.append(res)
                return
            for i in "()":
                if l==r:
                    if l!=0 and i=="(":
                        func(l-1,r,res+i)
                else:
                    if i=="(":
                        if l!=0:
                            func(l-1,r,res+i)
                    else:
                        if r!=0:
                            func(l,r-1,res+i)
        func(n,n,"")
        print(ans)
        return ans