class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def func(start,res):
            nonlocal ans
            ans.append(res.copy())
            for i in range(start, len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                res.append(nums[i])
                func(i+1, res)
                res.pop()
        func(0,[])
        print(ans)
        return ans