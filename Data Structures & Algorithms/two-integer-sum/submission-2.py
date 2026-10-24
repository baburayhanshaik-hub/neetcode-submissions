class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        for i in range(n):
            if target-nums[i] in d:
                return sorted([i,d[target-nums[i]]])
            d[nums[i]]=i
        