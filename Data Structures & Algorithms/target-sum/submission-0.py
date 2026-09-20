class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        visited = {}
        def func(i, target):
            if (i,target) in visited:
                return visited[(i,target)]
            if i==len(nums):
                if target == 0:
                    return 1
                return 0
            visited[(i,target)] = func(i+1,target-nums[i]) + func(i+1, target+nums[i])
            return visited[(i,target)]
        return func(0,target)