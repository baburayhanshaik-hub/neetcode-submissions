class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ncs = len(candidates)
        def func(nums,t):
            nonlocal ans
            s_nums = sum(nums)
            if s_nums>target:
                return
            if s_nums == target:
                ans.append(nums)
            for i in range(t,ncs):
                func(nums+[candidates[i]],i)
        func([],0)
        return ans