class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = r = 1
        ans = nums[0]
        res = ans
        while r<len(nums):
            if ans>=0:
                ans+=nums[r]
            else:
                l=r
                if r<len(nums):
                    ans = nums[r]
            res = max(ans,res)
            r+=1
        return res