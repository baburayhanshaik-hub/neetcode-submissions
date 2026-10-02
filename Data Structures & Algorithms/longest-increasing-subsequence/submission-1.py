class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [1 for i in range(len(nums))]
        visited = {}
        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if nums[j]<nums[i]:
                    ans[i]=max(ans[i],ans[j]+1)
        return max(ans)