class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def func(res,target):
            nonlocal ans
            if res == []:
                ans.append(target.copy())
            for i in range(len(res)):
                target+=[res[i]]
                func(res[:i]+res[i+1:],target)
                target.pop()
        func(nums,[])
        return ans