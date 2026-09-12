class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if digits == "":
            return []
        ans = []
        def func(res,n):
            nonlocal ans
            if n>=len(digits):
                ans.append(res)
                return
            for i in nums[int(digits[n])]:
                func(res+i,n+1)
        func("",0)
        return ans